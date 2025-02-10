import hashlib
import random
import string

from dotenv import load_dotenv
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.entity.profile import Profile
from account.repository.account_repository_impl import AccountRepositoryImpl
from account.repository.profile_repository_impl import ProfileRepositoryImpl
from account.serializers import AccountSerializer
from account.service.account_service_impl import AccountServiceImpl
from redis_service.service.redis_service_impl import RedisServiceImpl


class AccountView(viewsets.ViewSet):
    accountService = AccountServiceImpl.getInstance()
    profileRepository = ProfileRepositoryImpl.getInstance()
    accountRepository = AccountRepositoryImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    load_dotenv()   # load all the variables at .env file

    def checkEmailDuplication(self, request):
        print("checkEmailDuplication()")

        try:
            print(f"request.data: {request.data}")
            email = request.data.get("email")
            print(f"email: {email}")
            isDuplicate = self.accountService.checkEmailDuplication(email)
            print(f"isDuplicate: {isDuplicate}")

            return Response(
                {
                    "isDuplicate": isDuplicate,
                    "message": (    # isDuplicate이면 이미 존재/ 아니라면 사용 가능
                        "Email이 이미 존재" if isDuplicate else "Email 사용 가능"
                    ),
                },
                status=status.HTTP_200_OK,
            )
        
        except Exception as e:
            print("이메일 중복 체크 중 에러 발생:", e)
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def checkNicknameDuplication(self, request):
        print("checkNicknameDuplication()")

        try:
            nickname = request.data.get("newNickname")
            print(f"nickname: {nickname}")
            isDuplicate = self.accountService.checkNicknameDuplication(
                nickname
            )

            return Response(
                {
                    "isDuplicate": isDuplicate,
                    "message": (
                        "Nickname이 이미 존재" 
                        if isDuplicate else "Nickname 사용 가능"
                    ),
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print("닉네임 중복 체크 중 에러 발생:", e)
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def registerAccount(self, request):
        try:
            nickname = request.data.get("nickname")
            email = request.data.get("email")
            password = request.data.get("password")
            gender = request.data.get("gender")  # 성별 추가
            birthyear = request.data.get("birthyear")  # 생년월일 추가
            loginType = request.data.get("loginType")   

            # ascii + digits + 구두점
            randomString = string.ascii_letters \
                        + string.digits \
                        + string.punctuation
            salt = ''.join(random.choice(randomString) for _ in range(16))

            # utf-8로 encode된 password
            encodedPassword = salt.encode("utf-8") + password.encode("utf-8")   
            hashedPassword = hashlib.sha256(encodedPassword)    
            password = hashedPassword.hexdigest()

            if loginType == "NORMAL":   # NORMAL이 login한다면
                account = self.accountService.registerAccount(
                    loginType=loginType,
                    roleType="NORMAL",
                    nickname=nickname,
                    email=email,
                    password=password,
                    salt=salt,
                    gender=gender,
                    birthyear=birthyear,
                )
            
            # email이 aim-sniper@kakao.com이라면 ADMIN(관리자)
            elif email == "aim-sniper@kakao.com":   
                account = self.accountService.registerAccount(
                    loginType=loginType,
                    roleType="ADMIN",
                    nickname=nickname,
                    email=email,
                    password=None,
                    salt=None,
                    gender=gender,
                    birthyear=birthyear,
                )

            else:
                account = self.accountService.registerAccount(
                    loginType=loginType,
                    roleType="NORMAL",
                    nickname=nickname,
                    email=email,
                    password=None,
                    salt=None,
                    gender=gender,
                    birthyear=birthyear,
                )

            serializer = AccountSerializer(account)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("계정 생성 중 에러 발생:", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def getNickname(self, request):
        email = request.data.get("email")
        # 요청한 email이 없다면 None, 200(OK)
        if not email:
            return Response(None, status=status.HTTP_200_OK)
        
        profile = self.profileRepository.findByEmail(email)
        # profileRepository에 profile이 없다면 NOT_FOUND(404)
        if profile is None:
            return Response(
                {"error": "Profile not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )  # 에러 처리 추가
        
        # 프로필의 nickname 등록
        nickname = profile.nickname
        return Response(nickname, status=status.HTTP_200_OK)

    # def getEmail(self, request):
    #     userToken = request.data.get("userToken")
    #     if not userToken:
    #         return Response(None, status=status.HTTP_200_OK)
    #     accountId = self.redisService.getValueByKey(userToken)
    #     profile = self.profileRepository.findById(accountId)
    #     if profile is None:
    #         return Response(
    #             {"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND
    #         )  # 에러 처리 추가
    #     email = profile.email
    #     return Response(email, status=status.HTTP_200_OK)

    def withdrawAccount(self, request):
        try:
            # Account 정보를 인출하려는 이유(withdrawReason)
            withdrawReason = request.data.get("reason")
            print(f"reason: {withdrawReason}")

            userToken = request.data.get("userToken")
            if not userToken:   # userToken이 없다면 None, OK(200)
                return Response(None, status=status.HTTP_200_OK)

            # accountId와 account에 대한 정보를 각각 가져옴
            accountId = self.redisService.getValueByKey(userToken)
            account = self.accountRepository.findById(accountId)
            if account is None: # 만약 account가 None(없다면)-> NOT FOUND(404)
                return Response(
                    {"error": "Account not found"}, 
                    status=status.HTTP_404_NOT_FOUND
                )

            # 인출한 account에서 accountId와 withdrawReason을 각각 가져옴
            res = self.accountService.withdrawAccount(
                accountId, 
                withdrawReason
            )
            print(f"account: {account}")
            # account와 withdrawReason을 정상적으로 가져올 수 있다면 OK(200)
            return Response(res, status=status.HTTP_200_OK)
        
        except Exception as e:
            print("회원 탈퇴 중 에러 발생:", e)
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def getGender(self, request):
        email = request.data.get("email")
        if not email:   # email이 None이라면 OK(200)    
            return Response(None, status=status.HTTP_200_OK)
        
        profile = self.profileRepository.findByEmail(email)
        if profile is None: # profileRepository에 요청한 profile이 없다면 
            return Response(
                {"error": "Profile not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )  # 에러 처리 추가
        
        # genderId와 profileGenderType을 각각 가져옴
        genderId = profile.gender_id
        profileGenderType = self.profileRepository.findGenderTypeByGenderId(
            genderId    # male or female
        )
        genderType = profileGenderType.gender_type
        # genderType을 정상적으로 가져올 수 있다면 OK(200).
        return Response(genderType, status=status.HTTP_200_OK)

    def getBirthyear(self, request):
        email = request.data.get("email")
        if not email:   # email이 None하다면, 200_OK
            return Response(None, status=status.HTTP_200_OK)
        
        # profileRepository에 요청한 profile이 없는 경우 4040_error
        profile = self.profileRepository.findByEmail(email)
        if profile is None:
            return Response(
                {"error": "Profile not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )  # 에러 처리 추가
        
        birthyear = profile.birthyear
        # birthyear를 정상적으로 가져올 수 있다면 200_OK
        return Response(birthyear, status=status.HTTP_200_OK)

    def checkPassword(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            profile = Profile.objects.get(email=email)
            salt = profile.salt
            hashed = salt.encode('utf-8') + password.encode("utf-8")
            hash_obj = hashlib.sha256(hashed)
            password = hash_obj.hexdigest()

            isDuplicate = self.accountService.checkPasswordDuplication(
                email, password # email, password가 중복되는지 확인
            )

            return Response(
                {
                    'isDuplicate': isDuplicate, 
                    'message': 'password가 이미 존재' 
                    if isDuplicate else 'password 사용 가능'
                }, 
                status=status.HTTP_200_OK
            )
        
        except Exception as e:
            print("password 중복 체크 중 에러 발생:", e)
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def modifyNickname(self,request):
        # email과 newNickname을 각각 가져옴.
        email = request.data.get('email')
        newNickname = request.data.get('newNickname')

        # emial이 None하다면 200_OK.
        if not email:
            return Response(None, status=status.HTTP_200_OK)
        
        # profileRepository에서 요청한 profile이 없다면 404_error
        profile = self.profileRepository.findByEmail(email)
        if profile is None:
            return Response(
                {"error":"Profile not found"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        profile.nickname = newNickname
        # profile에 newNickname(modify한 nickname)을 저장
        profile.save()
        print(f"nickname: {profile.nickname}")
        return Response(profile.nickname, status=status.HTTP_200_OK)
    
    def modifyPassword(self,request):
        email = request.data.get('email')
        newPassword = request.data.get('newPassword')
        profile = Profile.objects.get(email=email)
        salt = profile.salt
        print(salt)
        hashed = salt.encode('utf-8') + newPassword.encode("utf-8")
        hash_obj = hashlib.sha256(hashed)
        newpassword1 = hash_obj.hexdigest()

        # emial이 없다면 202_ok
        if not email:
            return Response(None,status=status.HTTP_200_OK)
        
        # profileRepository에 요청한 profile이 없다면 404_error
        profile = self.profileRepository.findByEmail(email)
        if profile is None:
            return Response(
                {"error":"Profile not found"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        profile.password = newpassword1
        # newpassword1 저장
        profile.save()
        print(f"newPassword: {profile.password}")
        return Response(profile.password, status=status.HTTP_200_OK)

    def getAccountId(self, request):
        email = request.data.get("email")
        if not email:
            return Response(None, status=status.HTTP_200_OK)
        
        profile = self.profileRepository.findByEmail(email)
        if profile is None:
            return Response(
                {"error": "Profile not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )  # 에러 처리 추가
        
        accountId = profile.account_id
        return Response(
            {"accountId" : accountId}, 
            status=status.HTTP_200_OK
        )

    def getRoleType(self,request):
        email = request.data.get("email")
        if not email:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)
        
        roleType = self.accountService.findRoleTypeByEmail(email)
        return Response(
            {'roleType':str(roleType)},
            status=status.HTTP_200_OK
        )

    def getProfile(self, request):
        email = request.data.get("email")
        if not email:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)

        profile = self.accountService.findProfileByEmail(email)
        if profile is None:
            return Response(
                {'error': 'Profile not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )

        # 필요한 필드만 반환, gender 필드를 문자열로 변환
        profile_data = {
            'email': profile.email,
            'nickname': profile.nickname,
            'gender': str(profile.gender),  # 문자열로 변환
            'birthyear': profile.birthyear
        }
        return Response(profile_data, status=status.HTTP_200_OK)
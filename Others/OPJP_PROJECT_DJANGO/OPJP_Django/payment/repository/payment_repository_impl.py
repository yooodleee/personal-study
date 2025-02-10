import base64
import requests

from OPJP_Django import settings
from payment.repository.payment_repository import PaymentRepository


class PaymentRepositoryImpl(PaymentRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
            cls.__instance.paymentApiBaseUrl = settings.TOSS_PAYMENT['TOSS_PAYMENT_BASE_URL']
            cls.__instance.paymentApiSecretKey = settings.TOSS_PAYMENT['TOSS_PAYMENT_SECRET_KEY']

        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    
    def create(self, payment):
        try:
            # DB에 결제 정보 저장
            payment.save()  # Payment 모델의 save 메서드를 호출하여 저장
            return payment  # 저장된 객체 반환
        
        except Exception as e:
            print(f"결제 정보 저장 중 오류 발생: {e}")
            return None
    
    def request(self, paymentRequestData):
        try:
            # API 요청을 위한 헤더와 데이터 설정
            headers = {
                'Authorization': f"Basic {self.__getEncryptedSecretKey()}",
                "Content_Type": "application/json",
            }

            response = requests.post(
                f"{self.paymentApiBaseUrl}",
                headers=headers,
                json=paymentRequestData,
            )

            print(
                f"Response Status Code: {response.status_code}"
            )
            print(
                f"Response Headers: {response.headers}"
            )
            print(
                f"Response Body: {response.text}"
            )

            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(
                    f"API 요청 실패: {response.json().get("message")}"
                )
        except Exception as e:
            print(f"결제 요청 중 오류 발생: {e}")
            return None
    
    def __getEncryptedSecretKey(self):
        # 비밀 키 암호화
        secretKey = self.paymentApiSecretKey
        secretKeyBytes = (secretKey + ":").encode('utf-8')  # ":"를 추가하여 인코딩 준비
        encryptedSecretKey = base64.b64encode(
            secretKeyBytes
        ).decode('utf-8')   # Base64로 인코딩 후 문자열로 반환
        return encryptedSecretKey
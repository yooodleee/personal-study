<template>
    <div></div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

const naverAuthenticationModule = 'naverAuthenticationModule'
const accountModule = 'accountModule'

export default {
    computed: {
    ...mapState(accountModule, ["loginType"]),
    },
    methods: {
        ...mapActions(naverAuthenticationModule,
        ['requestNaverAccessTokenToDjangoRedirection', 'requestNaverUserInfoToDjango', 'requestAddNaverRedisAccessTokenToDjango']),
        ...mapActions(accountModule, ['requestEmailDuplicationCheckToDjango','requestRoleTypeToDjango']),

        async setRedirectData () {
            const code = this.$route.query.code
            await this.requestNaverAccessTokenToDjangoRedirection({ code })
            const naverUserInfo = await this.requestNaverUserInfoToDjango()
            if (!naverUserInfo) {
                console.error('userInfo is undefined.')
                return
            }
            // console.log('naverUserInfo:', naverUserInfo)

            const email = naverUserInfo.response.email
            // console.log('email: ', email)

            const isEmailDuplication = await this.requestEmailDuplicationCheckToDjango({ email })
            if (isEmailDuplication === true) {
                // console.log('기존 가입 고객입니다.')
                const accessToken = sessionStorage.getItem("naverAccessToken");
                
                if (accessToken) {
                    await this.requestAddNaverRedisAccessTokenToDjango({ email, accessToken });  // Fix: Pass as object directly
                } else {
                    console.error('AccessToken is missing');
                }
                const roleType = await this.requestRoleTypeToDjango(email)
                console.log(roleType.data.roleType)
                if (roleType.data.roleType == "ADMIN"){
                    sessionStorage.setItem('adminToken',sessionStorage.getItem('userToken'))
                    sessionStorage.removeItem('userToken')
                    this.REQUEST_IS_GOOGLE_AUTHENTICATED_TO_DJANGO(false);
                    this.REQUEST_IS_GOOGLE_ADMIN_TO_DJANGO(true);
                }
                sessionStorage.setItem('loginType', 'NAVER')
                sessionStorage.setItem('email', email)
                this.$router.push('/')
            } else {
                // console.log('신규 가입 고객입니다.')
                this.$router.push('/account/register')
            }
        }
    },
    async created () {
        await this.setRedirectData()
    }
}
</script>
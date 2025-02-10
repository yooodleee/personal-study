<template>
    <div></div>
</template>

<script>
import { mapActions, mapMutations, mapState } from 'vuex'

const googleAuthenticationModule = 'googleAuthenticationModule'
const accountModule = 'accountModule'

export default {
    computed: {
    ...mapState(accountModule, ["loginType"]),
    },
    methods: {
        ...mapActions(googleAuthenticationModule,
        ['requestGoogleAccessTokenToDjangoRedirection', 'requestGoogleUserInfoToDjango', 'requestAddGoogleRedisAccessTokenToDjango']),
        ...mapActions(accountModule, ['requestEmailDuplicationCheckToDjango',"requestRoleTypeToDjango"]),
        ...mapMutations(googleAuthenticationModule,['REQUEST_IS_GOOGLE_AUTHENTICATED_TO_DJANGO','REQUEST_IS_GOOGLE_ADMIN_TO_DJANGO']),
        async setRedirectData () {
            const code = this.$route.query.code
            await this.requestGoogleAccessTokenToDjangoRedirection({ code })
            const googleUserInfo = await this.requestGoogleUserInfoToDjango()
            if (!googleUserInfo) {
                console.error('userInfo is undefined.')
                return
            }
            // console.log('googleUserInfo:', googleUserInfo)

            const email = googleUserInfo.email
            // console.log('email: ', email)

            const isEmailDuplication = await this.requestEmailDuplicationCheckToDjango({ email })
            if (isEmailDuplication === true) {
                // console.log('기존 가입 고객입니다.')
                const accessToken = sessionStorage.getItem("googleAccessToken");
                
                if (accessToken) {
                    await this.requestAddGoogleRedisAccessTokenToDjango({ email, accessToken });  // Fix: Pass as object directly
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
                sessionStorage.setItem('loginType', 'GOOGLE')
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
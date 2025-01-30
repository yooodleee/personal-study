<template>
    <div></div>
</template>

<script>
import { mapActions, mapMutations, mapState } from 'vuex'

const authenticationModule = 'authenticationModule'
const accountModule = 'accountModule'

export default {
    computed: {
    ...mapState(accountModule, ["loginType"]),
    },
    methods: {
        ...mapActions(authenticationModule,
        ['requestAccessTokenToDjangoRedirection', 'requestUserInfoToDjango', 'requestAddRedisAccessTokenToDjango']),
        ...mapActions(accountModule, ['requestEmailDuplicationCheckToDjango','requestRoleTypeToDjango']),
        ...mapMutations(authenticationModule,['REQUEST_IS_AUTHENTICATED_TO_DJANGO','REQUEST_IS_ADMIN_TO_DJANGO']),
        async setRedirectData () {
            const code = this.$route.query.code
            await this.requestAccessTokenToDjangoRedirection({ code })
            const userInfo = await this.requestUserInfoToDjango()
            const email = userInfo.kakao_account.email
            // console.log('email: ', email)

            const isEmailDuplication = await this.requestEmailDuplicationCheckToDjango({ email })
            if (isEmailDuplication === true) {
                // console.log('기존 가입 고객입니다.')
                const accessToken = sessionStorage.getItem("accessToken");
                
                if (accessToken) {
                    await this.requestAddRedisAccessTokenToDjango({ email, accessToken });  // Fix: Pass as object directly
                } else {
                    console.error('AccessToken is missing');
                }

                const roleType = await this.requestRoleTypeToDjango(email)
                // console.log(roleType.data.roleType)
                if (roleType.data.roleType == "ADMIN"){
                    sessionStorage.setItem('adminToken',sessionStorage.getItem('userToken'))
                    sessionStorage.removeItem('userToken')
                    this.REQUEST_IS_AUTHENTICATED_TO_DJANGO(false);
                    this.REQUEST_IS_ADMIN_TO_DJANGO(true);
                }
                sessionStorage.setItem('email', email)
                sessionStorage.setItem('loginType', 'KAKAO')

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
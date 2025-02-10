import NaverRedirection from "@/naverAuthentication/redirection/NaverRedirection.vue"

const NaverAuthenticationRoutes = [
    {
        path: '/naver_oauth/access-token',
        name: 'NaverRedirection',
        component: NaverRedirection
    },
]

export default NaverAuthenticationRoutes
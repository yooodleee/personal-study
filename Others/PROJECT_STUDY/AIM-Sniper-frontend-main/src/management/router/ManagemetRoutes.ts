import ManagementLogPage from "../pages/ManagementLogPage.vue"
import ManagementUserPage from "../pages/ManagementUserPage.vue"

const ManageMentRoutes = [
    {
        path: '/management/user',
        name: 'ManagementUser',
        component: ManagementUserPage
    },
    {
        path: '/management/log',
        name: 'ManagementLog',
        component: ManagementLogPage
    },
]

export default ManageMentRoutes
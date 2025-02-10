import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import SurveyRoutes from '@/survey/router/SurveyRoutes'
import AccountRoutes from '@/account/router/AccountRoutes'
import AuthenticationRoutes from '@/authentication/router/AuthenticationRoutes'
import GoogleAuthenticationRoutes from '@/googleAuthentication/router/GoogleAuthenticationRoutes'
import HomeRoutes from '@/home/router/HomeRoutes'
import NaverAuthenticationRoutes from '@/naverAuthentication/router/NaverAuthenticationRoutes'
import CompanyReportRoutes from '@/companyReport/router/companyReportRoutes'
import CartRoutes from '@/cart/router/CartRoutes'
import OrderRoutes from '@/order/router/OrderRoutes'
import AiInterviewRoutes from '@/aiInterview/router/AiInterviewRoutes'
import GuideRoutes from '@/guide/router/guideRoutes'
import ManageMentRoutes from '@/management/router/ManagemetRoutes'

const routes: Array<RouteRecordRaw> = [
  ...HomeRoutes,
  ...AccountRoutes,
  ...AuthenticationRoutes,  
  ...GoogleAuthenticationRoutes, 
  ...NaverAuthenticationRoutes,
  ...SurveyRoutes,
  ...CompanyReportRoutes,
  ...CartRoutes,
  ...OrderRoutes,
  ...AiInterviewRoutes,
  ...GuideRoutes,
  ...ManageMentRoutes
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
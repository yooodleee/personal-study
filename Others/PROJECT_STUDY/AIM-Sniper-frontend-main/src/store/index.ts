import surveyModule from '@/survey/store/surveyModule'
import accountModule from '@/account/store/accountModule'
import authenticationModule from '@/authentication/store/authenticationModule'
import googleAuthenticationModule from '@/googleAuthentication/store/googleAuthenticationModule'
import { createStore } from 'vuex'
import naverAuthenticationModule from '@/naverAuthentication/store/naverAuthenticationModule'
import companyReportModule from "@/companyReport/store/companyReportModule"
import cartModule from '@/cart/store/cartModule'
import orderModule from '@/order/store/orderModule'
import userLogModule from "@/userLog/store/userLogModule"
import aiInterviewModule from '@/aiInterview/store/aiInterviewModule'
import managementModule from '@/management/store/managementModule'

export default createStore({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    surveyModule,
    accountModule,
    authenticationModule,    
    googleAuthenticationModule,
    naverAuthenticationModule,
    companyReportModule,
    cartModule,
    orderModule,
    userLogModule,
    aiInterviewModule,
    managementModule
  }
})

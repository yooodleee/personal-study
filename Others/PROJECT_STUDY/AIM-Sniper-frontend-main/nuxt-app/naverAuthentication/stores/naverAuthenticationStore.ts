import { defineStore } from 'pinia';
import {naverAuthenticationState} from './naverAuthenticationstate'
import {naverAuthenticationAction} from './naverAuthenticationActions'

export const useNaverAuthenticationStore = defineStore('NaverAuthenticationStore', {
  state: naverAuthenticationState,
  actions: naverAuthenticationAction,
});
import { defineStore } from 'pinia';
import {authenticationState} from './authenticationState'
import {authenticationAction} from './authenticationActions'

export const useAuthenticationStore = defineStore('authenticationStore', {
  state: authenticationState,
  actions: authenticationAction,
});
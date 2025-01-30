import { defineStore } from 'pinia';
import {googleAuthenticationState} from './googleAuthenticationState'
import {googleAuthenticationActions} from './googleAuthenticationActions'

export const useGoogleAuthenticationStore = defineStore('GoogleAuthenticationStore', {
  state: googleAuthenticationState,
  actions: googleAuthenticationActions,
});
import { defineStore } from 'pinia';
import {managementState} from './managementState'
import { managementActions} from './managementActions';

export const useManagementStore = defineStore('managementStore', {
  state: managementState,
  actions: managementActions,
});
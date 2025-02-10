import { defineStore } from 'pinia';
import {CartState} from './cartState'
import {cartAction} from './cartActions'

export const useCartStore = defineStore('CartStore', {
  state: CartState,
  actions: cartAction,
});
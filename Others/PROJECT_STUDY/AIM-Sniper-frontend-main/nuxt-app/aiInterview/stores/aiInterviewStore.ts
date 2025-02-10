import { defineStore } from 'pinia';
import { aiInterviewActions } from './aiInterviewActions';
import { aiInterviewState } from './aiInterviewState';
                
export const useAiInterviewStore = defineStore('aiInterviewStore', {
    state: aiInterviewState,
    actions: aiInterviewActions
});
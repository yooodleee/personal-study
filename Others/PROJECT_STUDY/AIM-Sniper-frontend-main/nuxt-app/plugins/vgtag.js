// plugins/vgtag.js
import { defineNuxtPlugin } from '#app'
import { useRuntimeConfig } from 'nuxt/app';
import VueGtag from 'vue-gtag-next'

export default defineNuxtPlugin((nuxtApp) => {
  const isDev = process.env.NODE_ENV !== 'production'; // 개발 환경 체크
  const runtimeConfig = useRuntimeConfig();

  if (!isDev) {
    nuxtApp.vueApp.use(VueGtag, {
      property: {
        id: runtimeConfig.public.GA_MEASUREMENT_ID,
      },
    });
  }
});

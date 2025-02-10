import { defineNuxtConfig } from "nuxt/config";

export default defineNuxtConfig({
    compatibilityDate: '2024-11-01',
    devtools: { enabled: true },
    extends: [
        './pandas_basic.nuxt.config.ts',
        './account/nuxt.config.ts',
        './kakaoAuthentication/nuxt.config.ts',
    ],

    css: [
        'vuetify/styles',
        '@mdi/font/css/materialdesignicons.min.css',
    ],

    build: {
        transpile: ['vuetify']
    },

    vite: {
        ssr: {
            noExternal: ['vuetify'],
        },
    },

    modules: [
        'vuetify-nuxt-module',
        '@pinia/nuxt',
        '~/pandas_basic/index.ts',
        '~/account/index.ts',
        '~/kakaoAUthentication/index.ts',
    ],

    imports: {
        dirs: ['./stores']
    },

    runtimeConfig: {
        public: {
            MAIN_API_URL: process.env.VUE_APP_BASE_URL,
            AI_BASE_URL: process.env.VUE_APP_AI_BASE_URL,
        }
    },
})
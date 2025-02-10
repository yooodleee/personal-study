import { defineNuxtModule } from '@nuxt/kit';
import { resolve } from 'path';

export default defineNuxtModule({
    meta: {
        name: 'kakaoAuthentication',
        configKey: 'kakaoAuthentication',
    },

    setup(moduleOptions, nuxt) {
        const themeDir = resolve(__dirname, '..');

        nuxt.hook('pages:extend', (pages) => {
            pages.push({
                name: 'kakaoRedirection',
                path: '/kakao-oauth/redirect-access-token',
                file: resolve(themeDir, 'kakaoAuthentication/redirection/KakaoRedirection.vue'),
            });
        });

        nuxt.hook('imports:dirs', (dirs) => {
            dirs.push(resolve(__dirname, 'store'));
        });
    },
});
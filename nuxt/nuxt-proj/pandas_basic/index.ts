import { defineNuxtModule } from "nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule ({
    meta: {
        name: "pandas_basic",
        configKey: "pandas_basic"
    },

    setup(moduleOptions, nuxt) {
        const themDir = resolve(__dirname, '..');

        nuxt.hook('pages:extend', (pages) => {
            pages.push({
                name: 'pandas-basic-inco',
                path: '/pandas-basic/info',
                file: resolve(themDir, 'pandas_basic/pages/pandas-basic-info.vue'),
            });
        });

        nuxt.hook('imports:dirs', (dirs) => {
            dirs.push(resolve(__dirname, 'store'));
        });
    },
});
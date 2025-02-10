import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from 'path';

export default defineNuxtModule({
    meta: {
        name: 'CompanyReportPage',
        configKey: 'CompanyReportPage',
    },

    setup(moduleOptions, nuxt) {
        const themeDir = resolve(__dirname, '..')

        nuxt.hook('pages:extend', (pages) => {
            pages.push({
                name: 'CompanyReportPage',
                path: '/companyReport/list',
                file: resolve(themeDir, 'companyReport/pages/list/CompanyReportListPage.vue'),
            },
            {
                name: 'CompanyReportReadPage',
                path: '/companyReport/read/:id',
                file: resolve(themeDir, 'companyReport/pages/read/CompanyReportReadPage.vue'),
            },
            {
                name: 'CompanyReportModifyPage',
                path: '/companyReport/modify/:id',
                file: resolve(themeDir, 'companyReport/pages/modify/CompanyReportModifyPage.vue'),
            }
            )
        })

        nuxt.hook('imports:dirs', (dirs) => {
            dirs.push(resolve(__dirname, 'store'))
        })
    },
})
import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule({
	meta: {
		name: "survey",
		configKey: "survey",
	},

	setup(moduleOptions, nuxt) {
		const themeDir = resolve(__dirname, "..");

		nuxt.hook("pages:extend", (pages) => {
			pages.push(
				{
					name: "SurveyRegisterPage",
					path: "/survey/register",
					file: resolve(
						themeDir,
						"survey/pages/register/SurveyRegisterPage.vue"
					),
				},
                {
					name: "SurveyReadPage",
					path: "/survey/read/:randomString",
					file: resolve(themeDir, "survey/pages/read/SurveyReadPage.vue"),
				},
                {
                    name: 'SurveyCreatedPage',
                    path: '/survey/created',
                    file: resolve(themeDir, "survey/pages/created/SurveyCreatedPage.vue"),
                },            
                {
					name: "SurveyListPage",
					path: "/survey/list",
					file: resolve(themeDir, "survey/pages/list/SurveyListPage.vue"),
				},			
				{
                    name: 'SurveySubmittedPage',
                    path: '/survey/submitted',                    
                    file: resolve(themeDir, "survey/pages/submitted/SurveySubmittedPage.vue"),
                },
                {
                    name: 'SurveyResultPage',
                    path: '/survey/result/:surveyId',                    
                    file: resolve(themeDir, "survey/pages/result/SurveyResultPage.vue"),
                }
			);
		});

		nuxt.hook("imports:dirs", (dirs) => {
			dirs.push(resolve(__dirname, "store"));
		});
	},
});
import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule({
	meta: {
		name: "aiInterview",
		configKey: "aiInterview",
	},

	setup(moduleOptions, nuxt) {
		const themeDir = resolve(__dirname, "..");

		nuxt.hook("pages:extend", (pages) => {
			pages.push(
				// {
				// 	name: "AiInterviewPage",
				// 	path: "/ai-interview",
				// 	file: resolve(themeDir, "aiInterview/pages/AiInterviewPage.vue"),
				// },
				
				{
					name: "AIInterviewLLMTestPage",
					path: "/ai-interview",
					file: resolve(themeDir, "aiInterview/pages/llmTest/AIInterviewLLMTestPage.vue"),
				},
				{
					name: "AIInterviewAnswerResult",
					path: "/ai-interview/result/:accountId",
					file: resolve(themeDir, "aiInterview/pages/result/AIInterviewAnswerResultPage.vue"),
				}
			);
		});

		nuxt.hook("imports:dirs", (dirs) => {
			dirs.push(resolve(__dirname, "stores"));
		});
	},
});
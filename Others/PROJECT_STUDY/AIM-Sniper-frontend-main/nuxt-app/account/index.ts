import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule({
	meta: {
		name: "account",
		configKey: "account",
	},

	setup(moduleOptions, nuxt) {
		const themeDir = resolve(__dirname, "..");

		nuxt.hook("pages:extend", (pages) => {
			pages.push(
				{
					name: "AccountLoginPage",
					path: '/account/login',
					file: resolve(themeDir, "account/pages/login/AccountLoginPage.vue"),
				},
				{
					name: "AccountRegisterPage",
					path: '/account/register',
					file: resolve(
						themeDir,
						"account/pages/register/AccountRegisterPage.vue"
					),
				},
				{
					name: "AccountMyPage",
					path: '/account/mypage',
					file: resolve(themeDir, "account/pages/my/AccountMyPage.vue"),
				},
				{
					name: "AccountWithdrawPage",
					path: '/account/withdraw',
					file: resolve(
						themeDir,
						"account/pages/withdraw/AccountWithdrawPage.vue"
					),
				},
                {
					name: "AccountModifyPage",
					path: '/account/modify',
					file: resolve(
						themeDir,
						"account/pages/modify/AccountModifyPage.vue"
					),
				}
			);
		});

		nuxt.hook("imports:dirs", (dirs) => {
			dirs.push(resolve(__dirname, "store"));
		});
	},
});
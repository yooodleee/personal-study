import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule({
	meta: {
		name: "management",
		configKey: "management",
	},

	setup(moduleOptions, nuxt) {
		const themeDir = resolve(__dirname, "..");

		nuxt.hook("pages:extend", (pages) => {
			pages.push(
				{
					name: "managementUser",
					path: "/management/user",
					file: resolve(
						themeDir,
						"management/pages/managementUserPage.vue"
					),
				},
                {
					name: "managementLog",
					path: "/management/log",
					file: resolve(themeDir, "management/pages/managementLogPage.vue"),
				}
			);
		});

		nuxt.hook("imports:dirs", (dirs) => {
			dirs.push(resolve(__dirname, "store"));
		});
	},
});
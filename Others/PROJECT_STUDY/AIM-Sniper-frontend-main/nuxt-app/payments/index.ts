import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule({
	meta: {
		name: "payments",
		configKey: "payments",
	},

	setup(moduleOptions, nuxt) {
		const themeDir = resolve(__dirname, "..");

		nuxt.hook("pages:extend", (pages) => {
			pages.push(
				{
					name: "paymentsTestPage",
					path: "/payments/test/page",
					file: resolve(
						themeDir,
						"payments/pages/payment/testPayments.vue"
					),
				},
				{
					name: "paymentSuccessed",
					path: "/payment/success",
					file: resolve(
						themeDir,
						"payments/pages/succed/paymentSuccessed.vue"
					),
				},
				{
					name: "paymentFailed",
					path: "/payment/fail",
					file: resolve(
						themeDir,
						"payments/pages/failed/paymentFailed.vue"
					),
				}
			);
		});

		nuxt.hook("imports:dirs", (dirs) => {
			dirs.push(resolve(__dirname, "stores"));
		});
	},
});

import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule({
  meta: {
    name: "GoogleRedirection",
    configKey: "GoogleRedirection",
  },

  setup(moduleOptions, nuxt) {
    const themeDir = resolve(__dirname, "..");

    // pages:extend 훅 사용
    nuxt.hook("pages:extend", (pages) => {
      pages.push({
        name: "GoogleRedirection",
        path: "/google_oauth/access-token",
        file: resolve(themeDir, "googleAuthentication/redirection/googleAuthentication.vue"), // 경로 수정
      });
    });

    // store 폴더를 모듈로 추가
    nuxt.hook("imports:dirs", (dirs) => {
      dirs.push(resolve(__dirname, "store")); // store 디렉토리를 인식하도록 함
    });
  },
});

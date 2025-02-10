import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule({
  meta: {
    name: "Order",
    configKey: "Order",
  },

  setup(moduleOptions, nuxt) {
    const themeDir = resolve(__dirname, "..");

    // pages:extend 훅 사용
    nuxt.hook("pages:extend", (pages) => {
      pages.push({
        name: "OrderListPage",
        path: "/order/list",
        file: resolve(themeDir, "order/pages/list/orderListPage.vue"), // 경로 수정
      });
    });
    
    nuxt.hook("pages:extend", (pages) => {
        pages.push({
          name: "OrderReadPage",
          path: "/order/read/:ordersId",
          file: resolve(themeDir, "order/pages/read/orderReadPage.vue"), // 경로 수정
        });
      });

    // store 폴더를 모듈로 추가
    nuxt.hook("imports:dirs", (dirs) => {
      dirs.push(resolve(__dirname, "store")); // store 디렉토리를 인식하도록 함
    });
  },
});

<template>
    <div class="wrapper">
        <div class="box_section">
            <!-- 결제 UI -->
            <div id="payment-method"></div>
            <!-- 이용약관 UI -->
            <div id="agreement"></div>
            <!-- 쿠폰 체크박스
            <div style="padding-left: 33px">
                <div class="checkable typography--p">
                    <label for="coupon-box" class="checkable__label typography--regular">
                        <input :disabled="!inputEnabled" @change="updateAmount" id="coupon-box" class="checkable__input"
                            type="checkbox" aria-checked="true" /><span class="checkable__label-text"> 5원 쿠폰
                            적용</span>
                    </label>
                </div>
            </div> -->
            <!-- 결제하기 버튼 -->
            <v-btn :disabled="!inputEnabled" @click="requestPayment" class="button" id="payment-button"
                style="margin: 30px">결제하기</v-btn>
        </div>
    </div>
</template>

<script>
import { loadPaymentWidget, ANONYMOUS } from "@tosspayments/payment-widget-sdk";
import { useRuntimeConfig } from "nuxt/app";
import { nanoid } from "nanoid";
import { defineComponent, onMounted, ref } from "vue";
import { useRoute } from 'vue-router';

export default defineComponent({
    setup() {
        const config = useRuntimeConfig();
        const route = useRoute();

        const paymentWidget = ref(null)
        const paymentMethodWidget = ref(null)
        const clientKey = ref(config.public.TOSS_CLIENT_KEY)
        const customerKey = ref(null)
        const amount = ref(route.query.amount ? Number(route.query.amount) : 0); // 쿼리로 받은 금액을 사용, 없으면 0 기본값
        const inputEnabled = ref(false)
        const discountCouponAmount = ref(5)

        async function requestPayment() {
            try {
                if (paymentWidget.value) {
                    await paymentWidget.value.requestPayment({
                        orderId: nanoid(),
                        orderName: "AIM",
                        customerName: "AIM-sniper",
                        customerEmail: "abcdabcd@gmail.com",
                        customerMobilePhone: "01012341234",
                        successUrl: `${window.location.origin}/payment/success`,
                        failUrl: `${window.location.origin}/payment/fail`
                    })
                }
            } catch (error) {
                console.log(error)
            }
        }
        async function updateAmount() {
            const coupon = document.getElementById("coupon-box")
            if (coupon.checked == true) {
                amount.value -= discountCouponAmount.value
                paymentMethodWidget.value.updateAmount(amount.value);
            } else {
                paymentMethodWidget.value.updateAmount(amount.value);
            }
        }

        onMounted(async () => {
            paymentWidget.value = await loadPaymentWidget(clientKey.value, ANONYMOUS)
            paymentMethodWidget.value = paymentWidget.value.renderPaymentMethods("#payment-method", { value: amount.value }, { variantKey: "DEFAULT" })
            paymentWidget.value.renderAgreement("#agreement", { variantKey: "AGREEMENT" })
            paymentMethodWidget.value.on("ready", () => {
                inputEnabled.value = true
            })
        })

        return {
            paymentWidget,
            paymentMethodWidget,
            clientKey,
            customerKey,
            amount,
            inputEnabled,

            requestPayment,
            updateAmount,
        }
    }
})
</script>
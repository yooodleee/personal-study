<template>
    <!-- 결제 성공 시 -->
    <section v-if="confirmed == true">
        <div class="box_section" style="width: 600px">
            <img style="width: 100px" src="https://static.toss.im/illusts/check-blue-spot-ending-frame.png" />
            <h2>결제를 완료했어요</h2>

            <div class="p-grid typography--p" style="margin-top: 50px">
                <div class="p-grid-col text--left"><b>결제금액</b></div>
                <div class="p-grid-col text--right" id="amount">{{ jsonData.totalAmount }}원</div>
            </div>
            <div class="p-grid typography--p" style="margin-top: 10px">
                <div class="p-grid-col text--left"><b>주문번호</b></div>
                <div class="p-grid-col text--right" id="orderId">{{ jsonData.orderId }}</div>
            </div>
            <div class="p-grid typography--p" style="margin-top: 10px">
                <div class="p-grid-col text--left"><b>paymentKey</b></div>
                <div class="p-grid-col text--right" id="paymentKey" style="white-space: initial; width: 250px">{{
                    jsonData.paymentKey }}</div>
            </div>
            <div class="p-grid" style="margin-top: 30px">
                <button class="button p-grid-col5"
                    onclick="location.href='https://docs.tosspayments.com/guides/payment/integration';">연동 문서</button>
                <button class="button p-grid-col5" onclick="location.href='https://discord.gg/A4fRFXQhRu';"
                    style="background-color: #e8f3ff; color: #1b64da">실시간 문의</button>                
            </div>

            <div>
                <!-- 주문 목록 페이지로 이동하는 버튼 -->
                <button class="button p-grid-col5" @click="goToOrderList"
                    style="background-color: #d1e7ff; color: #0a58ca; margin-left: 10px;">주문 목록 보기</button>
            </div>
        </div>
            
        

        <div class="box_section" style="width: 600px; text-align: left">
            <b>Response Data :</b>
            <div id="response" style="white-space: initial">
                <pre>{{ jsonData }}</pre>
            </div>
        </div>
    </section>
</template>

<script>
import { defineComponent, onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useRuntimeConfig } from "nuxt/app";

export default defineComponent({
    setup() {
        const route = useRoute()
        const router = useRouter()
        const config = useRuntimeConfig()


        const confirmed = ref(false)
        const jsonData = ref(null)
        const secretKey = ref(config.public.TOSS_SECRET_KEY)

        async function confirmPayment(requestData) {
            const encryptedSecretKey = btoa(secretKey.value + ":")

            const response = await fetch("https://api.tosspayments.com/v1/payments/confirm", {
                method: "POST",
                headers: {
                    "Authorization": `Basic ${encryptedSecretKey}`,
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(requestData),
            })

            const json = await response.json()

            return { response, json }
        }
        async function confirm(requestData) {
            try {
                const { response, json } = await confirmPayment(requestData)
                if (!response.ok) {
                    router.push(`fail?message=${json.mesasge}&code=${json.code}`)
                } else {
                    confirmed.value = true
                    jsonData.value = true
                }
            } catch (error) {
                console.log(error)
            }
        }

        function goToOrderList() {
            router.push('/order/list')
        }

        onMounted(async () => {
            const requestData = {
                orderId: route.query.orderId,
                amount: route.query.amount,
                paymentKey: route.query.paymentKey,
            }
            confirm(requestData)
        })

        return {
            secretKey,
            confirmed,
            jsonData,
            confirmPayment,
            confirm,
            goToOrderList
        }
    }
})
</script>


<style scoped>
.box_section {    
    margin-top: 10%;
    margin-left: 42%;    
}
</style>
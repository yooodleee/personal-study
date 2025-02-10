<template>
    <v-app>
        <v-main class="library-background pa-0">
            <v-container fluid class="pa-0">
                <!-- 배경 이미지와 텍스트를 포함한 Hero 섹션 -->
                <v-row>
                    <v-col cols="12">
                        <v-img
                        src="@/assets/images/fixed/고양이 누끼.png"
                        width="100vw"  height="70vh" position="absolute"  top: 0;
                        left: 0
                        z-index: -1;  object-fit: cover;
                        >
                            <v-row class="fill-height ma-0" align="center" justify="center">
                                <v-col class="text-center">
                                    <v-btn color="primary" large class="mb-4">
                                        Get Started
                                    </v-btn>
                                </v-col>
                            </v-row>
                        </v-img>
                    </v-col>
                </v-row>

                <!-- 기능 카드 섹션 -->
                <v-row class="mt-6" align="start">
                    <v-col v-for="n in 4" :key="n" cols="12" sm="6" md="3">
                        <v-card>
                            <v-img
                                    src="https://picsum.photos/1600/900"
                                    height="200"
                            ></v-img>
                            <v-card-title class="text-h6">특징 {{ n }}</v-card-title>
                            <v-card-subtitle>
                                가즈아~ 지브로
                            </v-card-subtitle>
                            <v-card-actions>
                                <v-btn text>Learn More</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-col>
                </v-row>

                <!-- Footer 섹션 -->
                <v-row>
                    <v-col cols="12" class="text-center">
                        <v-divider></v-divider>
                        <p>&copy; OPJP. Library Service.</p>
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
export default {
    name: "HomePage"
}
</script>

<style>
.library-background {
  background-image: url('../../assets/images/fixed/도서관 배경사진.webp') !important;
  background-size: cover !important;
  background-position: center !important;
  background-attachment: fixed !important;
}

.v-application {
  margin: 0 !important;
  padding: 0 !important;
}

.v-container {
  margin: 0 !important;
  padding: 0 !important;
  max-width: 100% !important;
}
</style>
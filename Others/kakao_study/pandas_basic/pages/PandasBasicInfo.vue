<template>
    <v-container>
        <h2>Pandas Basic Info</h2>
        <v-list>
            <v-list-item
                v-for="pandasInfo in pandasInfoList"
                :key="pandasInfo.id"
            >
                <v-list-item-content>
                    <v-list-item-title>{{ pandasInfo.name }}</v-list-item-title>
                    <v-list-item-subtitle>{{ pandasInfo.age }}</v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>
        </v-list>
    </v-container>
</template>

<script>
import { defaultComponent } from '@vue/composition-api'
import { onMounted } from 'vue';

export default defineAsyncComponent({
    setup() {
        const pandasInfoList = ref([])
        const loading = ref(false)
        const error = ref(null)

        const fetchPandasInfo = async () => {
            loading.value = true
            try {
                const response = await fetch('http://localhost:8000/pandas-basic/request-pandas-info')

                if (!response.ok) {
                    throw new Error('Error: ${response.status}')
                }

                const data = await response.json()
                pandasInfoList.value = data.serializedPandasInfoList
            } catch(error) {
                error.value = err.message
            } finally {
                loading.value = false
            }
        }
        
        onMounted(fetchPandasInfo)

        return {
            pandasInfoList,
            loading,
            error,
        }
    },
})
</script>
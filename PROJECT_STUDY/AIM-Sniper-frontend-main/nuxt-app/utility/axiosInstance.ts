import axios, { type AxiosInstance } from "axios";
import { useRuntimeConfig } from "nuxt/app";
export let djangoAxiosInst: AxiosInstance | null = null;
export let fastapiAxiosInst: AxiosInstance | null = null;

export function createAxiosInstances() {
    const config = useRuntimeConfig();

    const mainApiUrl: string = config.public.MAIN_API_URL as string;
    const aiBaseUrl: string = config.public.AI_BASE_URL as string;

    if (!djangoAxiosInst) {
        djangoAxiosInst = axios.create({
            baseURL: mainApiUrl,
            timeout: 5000,
            headers: {
                'Content-Type': 'application/json',
            },
        });
    }

    if (!fastapiAxiosInst) {
        fastapiAxiosInst = axios.create({
            baseURL: aiBaseUrl,
            timeout: 10000,
        });
    }

    return { djangoAxiosInst, fastapiAxiosInst };
}
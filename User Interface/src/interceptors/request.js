export default function requestInterceptor(api){
    api.interceptors.request.use(config => {
        config.headers.Authorization = `Bearer ${window.accessToken}`
        return config
    })
}
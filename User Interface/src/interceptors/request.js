export default function requestInterceptor(api){
    let accessToken = localStorage.getItem("access_token")

    api.interceptors.request.use(config => {
        config.headers.Authorization = `Bearer ${accessToken}`
        return config
    })
}
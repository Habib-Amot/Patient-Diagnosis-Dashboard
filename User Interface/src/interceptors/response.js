import getAccessToken from "@/utils/getToken";

export default async function responseInterceptor(api){
    let responseSuccessInterceptor = response => response

    let responseErrorInterceptor = async (error) => {
        let originalRequest = error.config;
        // checking if the request has not been retried before
        if(!originalRequest._retry && error.response?.status == 401){
            originalRequest._retry = true;
            let newToken =  await getAccessToken()
            // appending the token into the request to be sent out again
            originalRequest.config.headers.Authorization = `Bearer ${newToken}`
            return await api.get(originalRequest)
        }

        // if the request is being tried already or status != 401
        return Promise.reject(error)
    }

    api.interceptors.response.use(responseSuccessInterceptor, responseErrorInterceptor)
}

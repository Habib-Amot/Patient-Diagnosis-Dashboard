import axios from "axios";
import responseInterceptor from "@/interceptors/response";

let apiCall = axios.create({
baseURL: "http://localhost:5173",
})

responseInterceptor(apiCall)  // registering response interceptor on api Object
export default apiCall

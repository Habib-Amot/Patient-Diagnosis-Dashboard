import apiCall from "./api"

export default async function getPatients(){
    let patientEndpoint = "/app/api/users"
    try{
        let response = await apiCall(patientEndpoint)
        return response.data
    }catch{
        console.log("Unable to fecth users")
    }
}
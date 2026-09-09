export const loginUser = async function(email, password){
    let authenticationEndpoint = 'http://127.0.0.1:8000/app/api/auth';
    try{
        let response = await fetch(authenticationEndpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({email:email, password:password}),
        })
        if(response.ok){
            let data = await response.json()
            return data
        }else if(response.status == 404){
            return {
            status: "FAILED", 
            detail: "Bad url endpoint"
          }
        }
    }
    catch{
        return {
            status: "FAILED", 
            details: "Unable to connect to server, check you internet connection or Wi-Fi settings"
        }
    };
    
}

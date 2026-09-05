async function getCSRFCookie(){
    let cookieEndpoint = 'http://127.0.0.1:8000/app/api/get-csrf-token'
        try{
            let response = await fetch(cookieEndpoint);
            let token = await response.json()
            console.log(token.value)
            return token.value
        }catch{
            return null
        }
}

export default getCSRFCookie
async function getAccessToken(){
    let accessTokenEndpoint = 'http://127.0.0.1:8000/app/api/tokens/refresh'
    let refreshToken = localStorage.getItem('refreshToken')

        try{
            let response = await fetch(accessTokenEndpoint, {
                method: "post",
                headers:{
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({refresh: refreshToken })
            });

            let token = await response.json()
            window.accessToken = (token)
            return token.value
        }catch{
            return null
        }
}

export default getAccessToken
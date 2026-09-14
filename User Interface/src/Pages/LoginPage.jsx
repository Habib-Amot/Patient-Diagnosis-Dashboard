import { loginUser } from "@/api/auth"
import NavBar from "@/components/Bar/NavBar"
import AuthContext from "@/context/Auth/contexts"
import { useContext, useState } from "react"
import { useNavigate } from "react-router-dom"
import UserContext from "@/context/User/context"

const LoginPage = () => {
  let navigate = useNavigate()
  let [ userEmail, setUserEmail ] = useState("")
  let [ authError, setAuthError ] = useState('')
  let { setIsLoggedIn} = useContext(AuthContext)
  let { setUsername } = useContext(UserContext)
  let [ userPassword, setUserPassword] = useState("")

  function handleUserInput(event, type){
    let value = event.target.value
    type == "email" ? setUserEmail(value) : setUserPassword(value)
  }

  async function handleSubmit(){
    try{
      let response = await loginUser(userEmail, userPassword)
      if(response.STATUS == "login successful".toUpperCase()){
        let accessToken = response.details.access_token
        localStorage.setItem("access_token", accessToken)
        let username = response.details.user
        
        setUsername(username)  // set the username in the context
        setIsLoggedIn(true)  // set the login state in the context
        
        // navigate to the home page
        navigate("/home")
      }else{
        setAuthError(response.detail)
      }

    }catch(e){
      console.log(e)
    }
  }
  return (
    <div className="flex flex-col h-full">
      <NavBar/>
      <div className="flex flex-col justify-center items-center grow h-100">
        <p>{authError}</p>
        <div className="max-w-200 w-120 h-120 flex flex-col items-center gap-5 bg-white py-10 px-8 rounded-md">
          <div className="w-full flex items-center justify-center">
            <h2 className="font-semibold text-3xl mb-5">Welcome Back</h2>
          </div>
          <div className="input-section flex flex-col gap-3 w-full">
            <p className="label">Email</p>
            <input className="border outline-0 border-gray-200 h-12 p-2 rounded-sm text-sm" type="email" name="email" placeholder="Enter your email" value={userEmail} onChange={(event)=>handleUserInput(event, 'email')}/>
          </div>

          <div className="input-section flex flex-col gap-3 w-full">
            <p className="label">Password</p>
            <input className="border outline-0 border-gray-200 h-12 p-2 rounded-sm text-sm" type="password" name="password" 
            placeholder="Enter your password" value={userPassword} onChange={(event)=> handleUserInput(event, "password")}/>
          </div>

          <button onClick={handleSubmit} className="w-full  h-12 bg-blue-600 text-white rounded-md">Continue</button>
          <p className="text-sm flex gap-2">
            Forgot password ?
            <a href="#" className="text-blue-600">contact admin</a>
          </p>

        </div>
      </div>
    </div>
  )
}

export default LoginPage

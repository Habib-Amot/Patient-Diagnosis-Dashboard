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
    <div>
      <NavBar/>
      <div className="flex flex-col justify-center items-center">
        <p>{authError}</p>
        <div>
          <div className="w-full">
            <h2>Welcome Back</h2>
          </div>
          <div className="input-section flex flex-col">
            <p className="label">Email</p>
            <input type="email" name="email" placeholder="Enter your email" value={userEmail} onChange={(event)=>handleUserInput(event, 'email')}/>
          </div>

          <div className="input-section flex flex-col">
            <p className="label">Password</p>
            <input type="password" name="password" 
            placeholder="Enter your password" value={userPassword} onChange={(event)=> handleUserInput(event, "password")}/>
          </div>

          <p>
            Forgot password ?
            <a href="#">contact admin</a>
          </p>

          <button onClick={handleSubmit}>Continue</button>

        </div>
      </div>
    </div>
  )
}

export default LoginPage

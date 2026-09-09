import { useContext, useEffect } from "react"
import AuthContext from "@/context/Auth/contexts"
import { useNavigate } from "react-router-dom"

const ProtectedRoute = ({children}) => {
    let { isLoggedIn } = useContext(AuthContext)
    let navigate = useNavigate()

    useEffect(()=>{
      !isLoggedIn && navigate('/app/login')
    }, [isLoggedIn])
  return (
    <div>
      { isLoggedIn && children }
    </div>
  )
}

export default ProtectedRoute

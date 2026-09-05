import { useContext } from "react"
import AuthContext from "@/context/Auth/contexts"

const ProtectedRoute = ({children}) => {
    let { isLoggedIn } = useContext(AuthContext)
  return (
    <div>
      {
        isLoggedIn ? children : "Please Login to access this page"
      }
    </div>
  )
}

export default ProtectedRoute

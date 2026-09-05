import { useState } from "react"
import AuthContext from "./contexts"

const AuthContextProvider = ({children}) => {
  let [ isLoggedIn, setIsLoggedIn ] = useState(false)

  return (
    <AuthContext.Provider value={{isLoggedIn, setIsLoggedIn}}>
        {children}
    </AuthContext.Provider>
  )
}

export default AuthContextProvider

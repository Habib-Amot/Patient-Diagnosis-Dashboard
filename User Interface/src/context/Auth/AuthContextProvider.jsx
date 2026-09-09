import { useState } from "react"
import AuthContext from "./contexts"

const AuthContextProvider = ({children}) => {
  let [ isLoggedIn, setIsLoggedIn ] = useState(false)
  let [ accessToken, setAccessToken ] = useState('')
  let [ refreshToken, setRefreshToken ] = useState('')
  let [ tokenExpiry, setTokenExpiry ] = useState(0)

  let contextValues = {
    isLoggedIn, setIsLoggedIn, accessToken, setAccessToken,
    refreshToken, setRefreshToken, tokenExpiry, setTokenExpiry
  }

  return (
    <AuthContext.Provider value={contextValues}>
        {children}
    </AuthContext.Provider>
  )
}

export default AuthContextProvider

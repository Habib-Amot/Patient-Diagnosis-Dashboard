import { useState } from "react"
import UserContext from "./context"

const UserContextProvider = ({children}) => {
    let [ userData, setUserData ] = useState({})

  return (
    <UserContext.Provider value={{userData, setUserData}}>
        {children}
    </UserContext.Provider>
  )
}

export default UserContextProvider

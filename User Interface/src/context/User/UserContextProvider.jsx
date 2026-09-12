import { useState } from "react"
import UserContext from "./context"

const UserContextProvider = ({children}) => {
    let [ userName, setUserName ] = useState({})

  return (
    <UserContext.Provider value={{userName, setUserName}}>
        {children}
    </UserContext.Provider>
  )
}

export default UserContextProvider

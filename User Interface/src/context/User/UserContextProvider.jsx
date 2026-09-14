import { useState } from "react"
import UserContext from "./context"

const UserContextProvider = ({children}) => {
    let [ userName, setUsername ] = useState({})

  return (
    <UserContext.Provider value={{userName, setUsername}}>
        {children}
    </UserContext.Provider>
  )
}

export default UserContextProvider

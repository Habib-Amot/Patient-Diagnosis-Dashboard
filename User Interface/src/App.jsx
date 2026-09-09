import { createBrowserRouter,  Route, createRoutesFromElements, RouterProvider } from 'react-router-dom'

import './App.css'
import LoginPage from '@/Pages/LoginPage'
import PatientsPage from '@/Pages/PatientsPage'
import ProtectedRoute from '@components/ui/ProtectedRoute'
import AuthContextProvider from '@/context/Auth/AuthContextProvider'
import UserContextProvider from '@/context/User/UserContextProvider'

function App() {
  let router = createBrowserRouter(
    createRoutesFromElements(
      <Route>
        <Route path='/' element={<ProtectedRoute><PatientsPage/></ProtectedRoute>}/>

        <Route path='/home' element={<ProtectedRoute><PatientsPage/></ProtectedRoute>}/>

        <Route path='/app/login' element={<LoginPage/>}/>
      </Route>
    )
  )

  return(
    <AuthContextProvider>
      <UserContextProvider>
        <RouterProvider router={router}/>
      </UserContextProvider>
    </AuthContextProvider>
  )
}

export default App

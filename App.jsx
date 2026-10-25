// import {userState} from "react"
// import Count from "./components/Count"
import { BrowserRouter, createBrowserRouter, Route, RouterProvider, Routes } from "react-router-dom"
import Navbar from "./components/Navbar"
import About from "./components/Pages/About"
import Home from "./components/Pages/Home"
import Contact from "./components/Pages/Contact"
import Layout from "./components/Layout"
import Notfound from "./components/Pages/Notfound"
import Userinfo from "./components/Pages/Userinfo"

function App() {
  let routes = createBrowserRouter([
    {
      path: "/",
      element: <Layout />,
      children: [
        {
          path: "/home",
          element: <Home />
        },
        {
          path: "/about",
          element: <About />
        },
        {
          path: "/contact",
          element: <Contact />
        },
        {
          path: "/user:user_Id",
          element:<Userinfo />
        },
        {
          path: "*",
          element: <Notfound />
        }
      ]
    },
  ])
  return (
    <>
      <RouterProvider router={routes} />
      {/* <Navbar /> */}
      {/* <Routes>
          <Route path="/home" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact/>} />
        </Routes> */}

      {/* <p className="text-4xl bg-[#5A3397] text-white p-10 text-center font-semibold ">
        Hello world!
      </p>
      <Count /> */}

      {/* <About/> */}
      {/* 
      <div className="grid sm:grid-cols-12 md:grid-cols-4 lg:grid-cols-6 grid-rows-4 bg-gray-300">
        <p className=" bg-blue-500">text-1</p>
        <p className=" bg-red-400">text-2</p>
        <p className="py-10 bg-yellow-900">text-3</p>
        <p className="py-10 bg-yellow-800">text-4</p>
        <p className="py-10 bg-yellow-700">text-5</p>
        <p className="py-10 bg-yellow-600">text-6</p>
        <p className="py-10 bg-yellow-500">text-7</p>
        <p className="py-10 bg-yellow-400">text-8</p>
        <p className="py-10 bg-yellow-300">text-9</p>
        <p className="py-10 bg-yellow-200">text-10</p>
        <p className="py-10 bg-yellow-150">text-11</p>
        <p className="py-10 bg-yellow-100">text-12</p>
        <p className="py-10 bg-yellow-900">text-13</p>
        <p className="py-10 bg-indigo -900">text-13</p>
      </div> */}
    </>
  )
}

export default App

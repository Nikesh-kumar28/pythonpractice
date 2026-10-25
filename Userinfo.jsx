import React from 'react'
import { useLocation, useParams } from 'react-router-dom'

function Userinfo() {
    let {id} = useParams()
    let {state} = useLocation()
    console.log("this is user in state", state, "userInfo")
    return (
        <div style={{ padding: "100px" }}>
            this is userInfo component
            <h1>{id}</h1>
            <p>{state?.name}</p>
            <p>{state?.username}</p>
            <p>{state?.email}</p>
        </div>
    )
}

export default Userinfo

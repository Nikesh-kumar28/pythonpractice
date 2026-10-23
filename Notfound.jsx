import React from 'react'
import { Link, useNavigate } from 'react-router-dom'

function Notfound() {
    let navigate = useNavigate()
    const handleGotoHome = () => {
        navigate('/')
    }
    return (
        <div style={{
            width: "500px",
            height: "500px",
            borderRadius: "20px",
            boxShadow: "5px 5px 8px gray",
            display: 'flex',
            justifyContent: "center",
            alignItems: "center",
            flexDirection: "column",
            margin: "100px auto"
        }}
        >
            <h1>404</h1>
            <p>not found</p>

            <button>
                <Link to={"/"}>Go to Home</Link>
            </button>

            <button
                style={{
                    padding: "3px 6px",
                    borderRadius: "10px",
                    backgroundColor: "green",
                    color: "white"
                }}
                onClick={handleGotoHome}
            >
                {"Home ----->"}
            </button>
        </div>
    )
}

export default Notfound

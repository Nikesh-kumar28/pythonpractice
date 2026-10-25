import React from 'react'
import { useNavigate } from 'react-router-dom';

function Users() {
    let navigate = useNavigate()
    const dummyUsers = [
        {
            id: 101,
            name: "Leanne Graham",
            username: "Bret",
            email: "sincere@april.biz",
            role: "Admin",
            active: true
        },
        {
            id: 102,
            name: "Ervin Howell",
            username: "Antonette",
            email: "Shanna@melissa.tv",
            role: "User",
            active: false
        },
        {
            id: 103,
            name: "Clementine Bauch",
            username: "Samantha",
            email: "Nathan@yesenia.net",
            role: "User",
            active: true
        }
    ];
    const handleUserClick = (user) => {
        console.log("user in handleUserClick", user)
        // navigate(`/user/${user.id}`)
        navigate(`/user/1`, {state:user})
    }
    return (
        <div
            style={{
                display: "flex",
                justifyContent: "center",
                flexWrap: "wrap",
                alignItems: "center",
                gap: "50px"
            }}
        >
            {dummyUsers.map((user, index) => {
                return (
                    <div
                        style={{
                            padding: "20px",
                            borderRadius: "10px",
                            boxShadow: "5px 5px 8px #c0bcbc",
                            backgroundColor: "#fff",
                            margin: "10px 0px",
                        }}
                        onClick={() => { handleUserClick(user) }}
                    >
                        <h1 style={{ fontWeight: "900", fontSize: "26px" }}> Name : {user.name}</h1>
                        <p> userName : {user.username}</p>
                        <p> email : {user.email}</p>
                    </div>
                )
            })}
        </div>
    )
}

export default Users

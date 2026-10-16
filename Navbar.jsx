function Navbar() {
    return <>
        <ul
        style={{
            display:"flex",
            gap:"20px",
            justifyContent:"center",
            backgroundColor:"#000",
            color: "#fff",
            padding: "10px"
        }}
        
        >
            <li>Home</li>
            <li><a href="http://localhost:5173/about">About</a></li>
            <li>Contact</li>
        </ul>
    </>

}

export default Navbar
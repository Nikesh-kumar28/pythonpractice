import { Link } from "react-router-dom"
function Navbar() {
    return(
         <>
         <ul
            style={{
                display: "flex",
                gap: "20px",
                justifyContent: "center",
                backgroundColor: "#000",
                color: "#fff",
                padding: "10px"
            }}
        >
            <li>
                <Link to={"/home"}>Home</Link>
            </li>

            {/* <li><a href="http://localhost:5173/about">About</a></li> */}
            <li>
                <Link to={"/about"}>About</Link>
            </li>
            <li>
                <Link to={"/contact"}>Contact</Link>
            </li>
        </ul>
         </>
    )
}
export default Navbar

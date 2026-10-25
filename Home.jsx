import Users from "./Users"

function Home() {
    return (
        <div
            style={{
                height: "90vh",
                backgroundColor: "green",
                display: "flex",
                justifyContent: "center",
                flexDirection:"column",
                alignItems: "center"
            }}
        >
            <h1 style={{ textAlign: "center", fontWeight: 900 }}>this is a home component</h1>
            <Users />
        </div>
    )
}

export default Home
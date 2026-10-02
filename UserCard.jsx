function UserCard({
    userName = "set your username",
    dob = "set your dob",
    email = "set your email",
    no = 0
}) {
    return <>
        <div style={{
            padding: "50px",
            borderRadius: "20px",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
            alignItems: "center",
            gap: "20px",
            boxShadow: "5px 5px 8px #d0d0d0",
            position: "relative",
            border: "1px solid gray"
        }}>
            <p
                style={{
                    position: "absolute",
                    top: 0,
                    left: 10
                }}>
                {no}
            </p>
            <p
                style={{
                    fontWeight: "900",
                    fontFamily: "sans-serif",
                    padding: "20px 0px"
                }}>
                {userName}
            </p>
            <p>{dob}</p>
            <p>{email}</p>
        </div>
    </>
}

export default UserCard 
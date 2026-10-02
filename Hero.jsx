import Card from "../Comman/Card"
import UserCard from "../Comman/UserCard"
let users = [

    { username: "alex01", dob: "1995-03-14", email: "alex01@example.com" },
    { username: "jordan02", dob: "1998-07-22", email: "jordan02@example.com" },
    { username: "sam03", dob: "1992-11-05", email: "sam03@example.com" },
    { username: "taylor04", dob: "2000-01-18", email: "taylor04@example.com" },
    { username: "morgan05", dob: "1997-09-30", email: "morgan05@example.com" },
    { username: "casey06", dob: "1994-05-11", email: "casey06@example.com" },
    { username: "riley07", dob: "1999-12-03", email: "riley07@example.com" },
    { username: "jamie08", dob: "1996-08-27", email: "jamie08@example.com" },
    { username: "drew09", dob: "1993-02-16", email: "drew09@example.com" },
    { username: "chris10", dob: "2001-06-09", email: "chris10@example.com" },
    { username: "morgan11", dob: "1995-10-25", email: "morgan11@example.com" },
    { username: "pat12", dob: "1991-04-07", email: "pat12@example.com" },
    { username: "devon13", dob: "1998-03-19", email: "devon13@example.com" },
    { username: "lee14", dob: "2000-11-28", email: "lee14@example.com" },
    { username: "robin15", dob: "1997-01-12", email: "robin15@example.com" },
    { username: "blake16", dob: "1994-06-21", email: "blake16@example.com" },
    { username: "quinn17", dob: "1999-09-15", email: "quinn17@example.com" },
    { username: "avery18", dob: "1996-12-31", email: "avery18@example.com" },
    { username: "cameron19", dob: "1992-07-08", email: "cameron19@example.com" },
    { username: "skyler20", dob: "2001-02-24", email: "skyler20@example.com" }


];
const Hero = () => {
    return <>
        <h1 style={{ textAlign: "center" }}>This is hero section</h1>
        <div
            style={{
                display: "flex",
                flexWrap: "wrap",
                gap: "30px",
                justifyContent: "space-around",
                padding: "50px 20px"
            }}
        >
            {/* <Card
                Profile={"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBvq26wOg0Zi4H-gLYQKJsHN1IhEoteb3j2cn9u__ifA&s=10"}
                Name={"Nikku"}
                Dob={"10-01-2006"}
                Add={"SFS Mansarovar"}
            />
            <Card
                Profile={"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNlE0Y7F1OlzQZzPNsvoGjXzntLZSQuRNoH2BlsmoeqQ&s=10"}
                Name={"Nikesh"}
                Dob={"10-01-2005"}
                Add={"Vijay Path Mansarovar"}
            />
            <Card
                Profile={"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-Ddn32YQ-sUT3riMT_EHKh0bpv6ateVvXuOqgaMEGUg&s=10"}
                Name={"Bhumika"}
                Dob={"10-01-2008"}
                Add={"Kiran Path Mansarovar"}
            /> */}

            {users.map((user, index) => {
                return <UserCard
                    userName={user?.username}
                    no={index + 1}
                    dob={user.dob}
                    email={user.email}
                />
            })}
        </div>
    </>
}

export default Hero
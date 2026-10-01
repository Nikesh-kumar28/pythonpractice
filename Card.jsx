import "./crd.css"
const Card = () => {
    return <>
        <style>{`
           #user_name{
            text-align: center;
           }
        `}</style>
        <div className="main_card">
            <img id="user_profile" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcIczUb2foz7_OFizYh5e0ZvDMH2iYIoVnVdDZ1OJNA9qd6GWObxz5CEnh&s=10" alt="" />
            <h5 id="user_name"> Nikesh Kumar</h5>
            <p>DOB : 28-04-2004</p>
            <p>Adress: Mansarovar jaipur </p>
        </div>
    </>
}

export default Card 
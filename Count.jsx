import { useState } from "react"
function Count() {
    // let count1 = 10

    // const [count1, setcount1] = useState(10)
    const [count1, setcount1] = useState(1)

    const handleDicClick = () => {
        // count1 = count1 - 1
        if (count1 > 5) {
            setcount1(count1 - 1)
        } else {
            console.log("count can not be less than 5")
        }
        // console.log("Dic Click", count1)
    }

    const handleIncClick = () => {
        if (count1 < 15) {
            setcount1(count1 + 1)
        } else {
            console.log("count can not be greater than 15")
        }
    }
    return <>
        <div>
            <h1
                style={{
                    textAlign: "center",
                    fontSize: "33px",
                    fontWeight: 900
                }}
            >
                this is counter project
            </h1>

            <h1
                style={{
                    textAlign: "center",
                    fontSize: "53px",
                    marginTop: "10px",
                    fontWeight: 900
                }}>
                {count1}
            </h1>

            <div style={{ display: "flex", justifyContent: "center", gap: "30px" }}>
                <button
                    style={{
                        backgroundColor: "red",
                        padding: "5px 20px",
                        fontSize: "22px",
                        borderRadius: "10px",
                        cursor: "pointer"
                    }}
                    onClick={handleDicClick}
                >
                    Dic --
                </button>
                <button
                    style={{
                        backgroundColor: "green",
                        padding: "5px 20px",
                        fontSize: "22px",
                        borderRadius: "10px",
                        cursor: "pointer"
                    }}
                    onClick={handleIncClick}
                >
                    Inc ++
                </button>
            </div>

        </div>
    </>
}

export default Count


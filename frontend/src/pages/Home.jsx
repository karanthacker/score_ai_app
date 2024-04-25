import { useState, useEffect } from "react";
import api from "../api";
import { Link } from "react-router-dom";

function Home() {
    const [questions, setQuestions] = useState([]);  // State to store the array of questions

    useEffect(() => {
        const fetchQuestions = async () => {
            try {
                const response = await api.get("/score/randomquestion/");
                console.log(response.data);
                setQuestions(response.data);  // Set the entire array to the state
            } catch (error) {
                console.error("Error fetching questions:", error);
            }
        };

        fetchQuestions();
    }, []);

    return (
        <div>
            <h1>Home Page</h1>
            {questions.map((question) => (
                <div key={question.id}>
                    <p>{question.question_text}</p>  
                </div>
            ))}
             <Link to="/logout" className="form-button">Logout</Link>
        </div>
        
    );
}
export default Home;
import { useState } from "react";
import ReactMarkdown from "react-markdown";

function App() {
const [question, setQuestion] = useState("");
const [answer, setAnswer] = useState("");
const [loading, setLoading] = useState(false);
const [error, setError] = useState("");

const handleAsk = async () => {
if (!question.trim()) {
setError("Please enter a question.");
return;
}


setLoading(true);
setError("");
setAnswer("");

try {
  const response = await fetch("http://127.0.0.1:8000/ask", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      question: question,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to get an answer from the server.");
  }

  const data = await response.json();

  setAnswer(data.answer);

} catch (error) {
  console.error("Error:", error);
  setError("Something went wrong. Please make sure the backend server is running.");

} finally {
  setLoading(false);
}

};

return ( <div className="container">


  <div className="card">

    <div className="header">
      <h1>College Placement AI</h1>

      <p>
        Ask questions about college placement policies.
      </p>
    </div>

    <textarea
      placeholder="Ask your question here..."
      value={question}
      onChange={(e) => setQuestion(e.target.value)}
    />

    <button
      onClick={handleAsk}
      disabled={loading}
    >
      {loading ? "Thinking..." : "Ask AI"}
    </button>

    {error && (
      <div className="error">
        {error}
      </div>
    )}

    {answer && (
      <div className="answer">

        <h2>AI Answer</h2>

        <div className="answer-content">
          <ReactMarkdown>
            {answer}
          </ReactMarkdown>
        </div>

      </div>
    )}

  </div>

</div>


);
}

export default App;

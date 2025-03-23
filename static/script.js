function askTutor() {
    let question = document.getElementById("query").value;
    if (!question.trim()) {
        alert("Please enter a question!");
        return;
    }

    fetch("https://your-backend-url.onrender.com/ask", { // UPDATE URL
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: question })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = "💡 AI Tutor: " + data.answer;
    })
    .catch(error => {
        document.getElementById("response").innerText = "❌ Error: Unable to get response.";
        console.error(error);
    });
}

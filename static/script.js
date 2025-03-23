function askTutor() {
    let query = document.getElementById("query").value;
    if (!query.trim()) {
        alert("Please enter a question!");
        return;
    }

    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: query })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("response").innerText = "❌ " + data.error;
        } else {
            document.getElementById("response").innerText = "💡 " + data.response;
        }
    })
    .catch(error => {
        document.getElementById("response").innerText = "❌ Error contacting server.";
    });
}

async function askTutor() {
    const query = document.getElementById("query").value;
    const responseElement = document.getElementById("response");

    if (!query.trim()) {
        responseElement.innerHTML = "❌ Error: Question cannot be empty!";
        return;
    }

    try {
        const response = await fetch("https://aixplain.onrender.com/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query: query }),
        });

        if (!response.ok) {
            throw new Error(`Server error! Status: ${response.status}`);
        }

        const data = await response.json();
        responseElement.innerHTML = `💡 AI Tutor: ${data.answer}`;
    } catch (error) {
        responseElement.innerHTML = "❌ Error: Unable to get response.";
        console.error("Fetch error:", error);
    }
}

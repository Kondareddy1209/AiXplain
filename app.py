from flask import Flask, render_template, request, jsonify
import os
from aixplain.factories import AgentFactory
from aixplain.modules import Tool

app = Flask(__name__)

# ✅ Set API Key
os.environ["TEAM_API_KEY"] = "fbe041c3fde606d4edb34f1482a64ebaf955fc93d7c2043bc3924c327aacbd44"

# ✅ AI Tutor Configuration
Name = "Virtual Tutor Agent"
Role = "An AI tutor that helps students by answering questions using Wikipedia and online resources."

# ✅ Initialize AI Tools
def load_tool(tool_id, tool_name):
    try:
        return Tool(id=tool_id)
    except Exception as e:
        print(f"⚠️ Failed to load {tool_name}: {e}")
        return None

wiki_tool = load_tool("6633fd59821ee31dd914e232", "Wikipedia Tool")
scraper_tool = load_tool("66f423426eb563fa213a3531", "Web Scraper")

# ✅ Create AI Tutor
try:
    tutor_agent = AgentFactory.create(
        name=Name,
        description=Role,
        tools=[t for t in [wiki_tool, scraper_tool] if t is not None]
    )
    print(f"✅ AI Tutor '{tutor_agent.name}' created successfully!")
except Exception as e:
    print(f"❌ Error creating AI tutor: {e}")
    tutor_agent = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask_question():
    if not tutor_agent:
        return jsonify({"error": "AI Tutor is not available."})

    user_query = request.json.get("query", "").strip()
    if not user_query:
        return jsonify({"error": "Empty query received!"})

    try:
        response = tutor_agent.run(user_query)
        return jsonify({"response": response["data"]["output"]})
    except Exception as e:
        return jsonify({"error": f"Error processing request: {e}"})

if __name__ == "__main__":
    app.run(debug=True)

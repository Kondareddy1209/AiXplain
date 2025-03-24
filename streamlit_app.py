from flask import Flask, render_template, request, jsonify
import os
from aixplain.factories import AgentFactory
from aixplain.modules import Tool

app = Flask(__name__)

API_KEY = os.getenv("TEAM_API_KEY", "")
if not API_KEY:
    print("❌ ERROR: TEAM_API_KEY is missing! Set it in Render's environment variables.")
else:
    os.environ["TEAM_API_KEY"] = API_KEY

Name = "Virtual Tutor Agent"
Role = "An AI tutor that helps students by answering questions using Wikipedia and online resources."

def load_tool(tool_id, tool_name):
    try:
        tool = Tool(id=tool_id)
        print(f"✅ {tool_name} loaded successfully!")
        return tool
    except Exception as e:
        print(f"⚠️ Failed to load {tool_name}: {e}")
        return None

wiki_tool = load_tool("6633fd59821ee31dd914e232", "Wikipedia Tool")
scraper_tool = load_tool("66f423426eb563fa213a3531", "Web Scraper")

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
        return jsonify({"error": "AI Tutor is not available."}), 500

    user_query = request.json.get("query", "").strip()
    if not user_query:
        return jsonify({"error": "Empty query received!"}), 400

    try:
        response = tutor_agent.run(user_query)
        return jsonify({"response": response["data"]["output"]})
    except KeyError:
        return jsonify({"error": "Unexpected response format from AI tool!"}), 500
    except Exception as e:
        return jsonify({"error": f"Error processing request: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

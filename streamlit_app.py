import os
import streamlit as st
from aixplain.factories import AgentFactory
from aixplain.modules import Tool

# Function to load API key from a file
def load_api_key(file_path="TEAM_API_KEY.txt"):
    try:
        with open(file_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        st.error("❌ Error: API key file not found!")
        return None

# Load API key
API_KEY = load_api_key()
if API_KEY:
    os.environ["TEAM_API_KEY"] = API_KEY
else:
    st.stop()  # Stop execution if API key is missing

# Define the AI tutor
st.title("🤖 AI Virtual Tutor")
st.write("Ask your questions and get AI-powered answers!")

query = st.text_input("Enter your question:")

# Load tools with correct initialization
def load_tool(tool_id, tool_name, tool_description):
    try:
        tool = Tool(id=tool_id, name=tool_name, description=tool_description)
        return tool
    except Exception as e:
        st.warning(f"⚠️ Failed to load {tool_name}: {e}")
        return None

wiki_tool = load_tool("6633fd59821ee31dd914e232", "Wikipedia Tool", "Fetches answers from Wikipedia.")
scraper_tool = load_tool("66f423426eb563fa213a3531", "Web Scraper", "Extracts data from web pages.")

# Debugging: Print tool status
st.write(f"📌 wiki_tool: {'Loaded' if wiki_tool else 'Failed'}")
st.write(f"📌 scraper_tool: {'Loaded' if scraper_tool else 'Failed'}")

# Ensure tools are available before creating an agent
valid_tools = [t for t in [wiki_tool, scraper_tool] if t is not None]

if not valid_tools:
    st.error("❌ No valid tools loaded! AI Tutor cannot be created.")
else:
    try:
        tutor_agent = AgentFactory.create(
            name="Virtual Tutor Agent",
            description="An AI tutor that helps students by answering questions using Wikipedia and online resources.",
            tools=valid_tools
        )
        st.success("✅ AI Tutor is ready!")
    except Exception as e:
        st.error(f"❌ Error creating AI tutor: {str(e)}")
        tutor_agent = None

# Handle user input and generate response
if query and tutor_agent:
    try:
        response = tutor_agent.run(query)
        output = response.get("data", {}).get("output", "No valid response received.")
        st.success(f"💡 AI Tutor: {output}")
    except KeyError:
        st.error("❌ Unexpected response format from AI tool!")
    except Exception as e:
        st.error(f"❌ Error processing request: {str(e)}")

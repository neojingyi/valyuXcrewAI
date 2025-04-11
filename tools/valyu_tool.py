import requests
import os
from crewai.tools.structured_tool import CrewStructuredTool
from pydantic import BaseModel, Field
from valyu import Valyu

class ValyuToolInput(BaseModel):
    query: str = Field(..., description="The user's question to be answered using the Valyu API")


def valyu_tool_runner(query: str) -> str:
    global valyu_tool_used
    valyu_tool_used = True
    api_key = os.getenv("VALYU_API_KEY")
    url = "https://api.valyu.network/v1/knowledge"
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "query": query,
        "search_type": "proprietary",
        "data_sources": [
            "valyu/valyu-arxiv",
            "valyu/valyu-wikipedia",
            "https://www.valyu.network/"
        ],
        "max_num_results": 5,
        "similarity_threshold": 0.4,
        "query_rewrite": True,
        "max_price": 123
    }


    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()

        if not data.get("results"):
            return "❌ No results found."
        summaries = []
        for result in data["results"][:3]:
            title = result.get("title", "Untitled")
            content = result.get("content", "")[:300].strip()
            url = result.get("url", "#")
            summaries.append(f"🔹 **{title}**\n{content}...\n🔗 [Read more]({url})\n")

        return "\n".join(summaries)

    except Exception as e:
        return f"❌ Error calling Valyu API: {str(e)}"

# Register the function as a CrewAI-compatible tool
def create_valyu_tool():
    return CrewStructuredTool.from_function(
        name="Valyu Knowledge Tool",
        description="Calls Valyu's proprietary API to retrieve factual answers to user questions.",
        args_schema=ValyuToolInput,
        func=valyu_tool_runner,
    )


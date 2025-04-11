import requests
import os
from crewai.tools.structured_tool import CrewStructuredTool
from pydantic import BaseModel, Field

class ValyuToolInput(BaseModel):
    query: str = Field(..., description="The user's question to be answered using the Valyu API")

def valyu_tool_runner(query: str) -> str:
    api_key = os.getenv("VALYU_API_KEY")
    if not api_key:
        return "Missing VALYU_API_KEY environment variable."

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
        for result in data["results"][:2]:
            title = result.get("title", "Untitled")
            content = result.get("content", "")[:100].strip()
            url = result.get("url", "#")
            summaries.append(f"🔹 **{title}**\n{content}...\n🔗 [Read more]({url})\n")

        return "\n".join(summaries)

    except requests.exceptions.Timeout:
        return "Valyu API request timed out."
    except requests.exceptions.ConnectionError:
        return "Network connection error while calling Valyu API."
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"
    

def create_valyu_tool():
    return CrewStructuredTool.from_function(
        name="Valyu Knowledge Tool",
        description="Calls Valyu's proprietary API to retrieve factual answers to user questions.",
        args_schema=ValyuToolInput,
        func=valyu_tool_runner,
    )


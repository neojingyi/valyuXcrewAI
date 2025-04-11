import requests
import os
from crewai.tools.structured_tool import CrewStructuredTool
from pydantic import BaseModel, Field

class ValyuToolInput(BaseModel):
    query: str = Field(..., description="The user's question to be answered using the Valyu API")

def valyu_tool_runner(query: str):
        api_key=os.getenv("VALYU_API_KEY")
        url="https://api.valyu.network/v1/knowledge"
        headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json"
            }
        payload = {
            "query": query,
            "search_type": "proprietary",
            "data_sources": ["valyu/valyu-arxiv", "valyu/valyu-wikipedia", "https://www.valyu.network/"],
            "max_num_results": 10,
            "similarity_threshold": 0.4,
            "query_rewrite": True,
            "max_price": 123
        }
        response = requests.post(url, json=payload, headers=headers)
        return response
        
def create_valyu_tool():
    return CrewStructuredTool.from_function(
        name= 'Valyu Knowledge Tool',
        description= "Calls Valyu's proprietary API to retrieve factual answers.",
        args_schema= ValyuToolInput,
        func= valyu_tool_runner,
    )
response = valyu_tool_runner("example query")
print(response.text)
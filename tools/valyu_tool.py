import requests
import os
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class ValyuToolInput(BaseModel):
    query: str = Field(..., description="The user's question to be answered using the Valyu API")

class ValyuTool(BaseTool):
    def _run(self,query,*args,**kwargs):
        return self.fetch_knowledge(query)

    def _run(self,query:str)-> str:
        api_key=os.getenv("VALYU_API_KEY")
        url="https://api.valyu.network/v1/knowledge"
        headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json"
            }
        payload = {
            "query": "<string>",
            "search_type": "proprietary",
            "data_sources": ["valyu/valyu-arxiv", "valyu/valyu-wikipedia", "https://www.valyu.network/"],
            "max_num_results": 10,
            "similarity_threshold": 0.4,
            "query_rewrite": True,
            "max_price": 123
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)
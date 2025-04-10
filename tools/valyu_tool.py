import requests
import os

class ValyuTool:
    def __init__(self):
        self.api_key=os.getenv("VALYU_API_KEY")

    def fetch_knowledge(self,query):
        url="https://api.valyu.network/v1/knowledge"
        headers = {
            "x-api-key": self.api_key,
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
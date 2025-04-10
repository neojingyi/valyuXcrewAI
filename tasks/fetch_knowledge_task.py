from crewai import Task
from agents.knowledge_agent import KnowledgeAgent
from tools.valyu_tool import ValyuTool

valyu_tool=ValyuTool()

def FetchKnowledgeTask(query):
    return Task(
        description=f"Use the Valyu API to answer this question:'{query}'",
        expected_output="A well explained, fact based answer.",
        tools=[{
            "name": "Valyu API Tool",
            "description": "Calls the Valyu API to retrieve facts.",
            "function": lambda: valyu_tool.fetch_knowledge(query)
        }],
        agent=KnowledgeAgent
    )
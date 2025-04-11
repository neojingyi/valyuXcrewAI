from crewai import Task
from agents.knowledge_agent import KnowledgeAgent
from tools.valyu_tool import create_valyu_tool

def FetchKnowledgeTask(query):
    valyu_tool = create_valyu_tool()
    return Task(
        description=f"Use the Valyu API to answer this question:'{query}'",
        expected_output="A well explained, fact based answer.",
        tools=[valyu_tool],
        agent=KnowledgeAgent
    )
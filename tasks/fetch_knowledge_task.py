from crewai import Task
from agents.knowledge_agent import KnowledgeAgent
from tools.valyu_tool import create_valyu_tool

def should_use_valyu(query: str) -> bool:
    keywords = ["research", "study", "paper", "neural", "theorem", "literature", "scientific"]
    return any(word in query.lower() for word in keywords)

def FetchKnowledgeTask(query):
    valyu_tool = create_valyu_tool()
    valyu_response=valyu_tool._run(query)
    if should_use_valyu(query):
        task_description = f"The user asked: '{query}'. Based on Valyu API, here's relevant data:\n\n{valyu_response}"
    else: 
        task_description = f"The user asked: '{query}'. Answering it without using external tools."
    return Task(
        description=task_description,
        expected_output="A well explained, fact based answer.",
        tools=[],
        agent=KnowledgeAgent
    )

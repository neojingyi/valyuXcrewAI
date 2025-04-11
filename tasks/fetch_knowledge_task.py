from crewai import Task
from agents.knowledge_agent import KnowledgeAgent
from tools.valyu_tool import create_valyu_tool

def should_use_valyu(query: str) -> bool:
    keywords = ["research", "study", "paper", "neural", "theorem", "literature", "scientific","valyu"]
    return any(word in query.lower() for word in keywords)

def FetchKnowledgeTask(query):
    valyu_tool = create_valyu_tool()
    if should_use_valyu(query):
        valyu_response=valyu_tool._run(query)
        task_description = (f"The user asked: '{query}'. Based on Valyu API, here's relevant data:\n\n{valyu_response}.\n"
                            "Use it to give concise answers, listing only the critical facts.\n"
                            "Limit the response to 2 short sentences, avoid repeating the question.")

    else: 
        task_description = (f"The user asked: '{query}'. Answering it without using external tools."
                            "Answer concisely using your own knowledge.\n"
                            "Limit the response to 2 short sentences, avoid repeating the question.")
    return Task(
        description=task_description,
        expected_output="A concise, factual answer in 2 short sentences",
        tools=[],
        agent=KnowledgeAgent
    )
from crewai import Crew
from tasks.fetch_knowledge_task import FetchKnowledgeTask
from dotenv import load_dotenv
from tools import valyu_tool
import os

load_dotenv()

def main():
    print("Ask me anything (type 'exit' to quit)\n")
    agents = []
    tasks = []
    while True:
        query = input("> ")
        if query.lower() in ['exit','quit']:
            print("Bye!")
            break
        task = FetchKnowledgeTask(query)
        MAX_HISTORY = 2
        agents.append(task.agent)
        tasks.append(task)
        if len(tasks) > MAX_HISTORY:
            agents = agents[-MAX_HISTORY:]
            tasks = tasks[-MAX_HISTORY:]
        crew = Crew(agents=agents, tasks=tasks, verbose=True, memory=True)
        result = crew.kickoff()
        print("\n Answer: \n", result)

if __name__ == "__main__":
    main()
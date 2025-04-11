from crewai import Crew
from tasks.fetch_knowledge_task import FetchKnowledgeTask
from dotenv import load_dotenv
from tools import valyu_tool
import os

load_dotenv()

def main():
    print("Ask me anything (type 'exit' to quit)\n")
    while True:
        query = input("> ")
        if query.lower() in ['exit','quit']:
            print("Bye!")
            break
        task=FetchKnowledgeTask(query)
        crew=Crew(agents=[task.agent],tasks=[task],verbose=True,memory=True)
        result = crew.kickoff()
        print("\n Answer: \n", result)

if __name__ == "__main__":
    main()
from crewai import Crew
from tasks.fetch_knowledge_task import FetchKnowledgeTask
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print("Ask me anything (type 'exit' to quit)\n")
    previous_answer=""
    while True:
        query = input("> ")
        if query.lower() in ['exit','quit']:
            print("Bye!")
            break
        full_query=f"{query}(based on:{previous_answer})"if previous_answer else query

        task=FetchKnowledgeTask(query)
        crew=Crew(agents=[task.agent],tasks=[task],verbose=True)
        result = crew.kickoff()
        print("\n Answer: \n", result)
        previous_answer=result

if __name__ == "__main__":
    main()
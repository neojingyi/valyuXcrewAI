from crewai import Crew
from tasks.fetch_knowledge_task import FetchKnowledgeTask
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Ask me a question:")
    query = input("> ")
    task=FetchKnowledgeTask(query)
    crew=Crew(agents=[task.agent],tasks=[task],verbose=True)
    result = crew.run()
    print("\n Answer: \n", result)

if __name__=="__main__":
    main()
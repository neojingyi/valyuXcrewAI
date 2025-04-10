from crewai import Agent

KnowledgeAgent = Agent(
    role='Information Specialist',
    goal='Answer questions accurately using real-time knowledge from Valyu.',
    backstory='You are an intelligent assistant who knows how to query the Valyu API.',
    allow_delegation=False,
    verbose=True
)

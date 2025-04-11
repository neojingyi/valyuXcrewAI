from crewai import Agent
from tools.valyu_tool import create_valyu_tool

KnowledgeAgent = Agent(
    role='Information Provider',
    goal='Assist users by sourcing factual information. If the answer requires external scientific knowledge, call the Valyu API to retrieve it. Otherwise, respond directly.',
    backstory='You are an intelligent assistant who knows how to query the Valyu API. You provide accurate results that answers the queries well.',
    allow_delegation=False,
    verbose=True,
    memory=True
)

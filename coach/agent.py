import os
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchResults
from langchain.agents import initialize_agent, Tool

def get_resources(subject: str, grade: str, goal: str):
    # Use a Groq model that’s currently active — change this as per your Groq dashboard
    llm = ChatGroq(model="llama-3.1-8b-instant", api_key=os.getenv("GROQ_API_KEY"))


    search = DuckDuckGoSearchResults()

    tools = [
        Tool(
            name="DuckDuckGo Search",
            func=search.run,
            description="Search the web for educational resources, pedagogy, and tools."
        )
    ]

    agent = initialize_agent(
        tools,
        llm,
        agent="zero-shot-react-description",
        verbose=True,
         handle_parsing_errors=True  
    )

    query = f"Find free teaching resources for {subject}, grade {grade}, goal {goal}"
    return agent.run(query)

from dotenv import load_dotenv
import os
from langchain.agents import initialize_agent, AgentType
from src.agents.prospect_discovery import ProspectDiscoveryAgent
from src.agents.validation_agent import ValidationAgent
from src.agents.outreach_agent import OutreachPersonalizationAgent
from src.agents.campaign_executor import CampaignExecutorAgent
from langchain.llms import OpenAI

# Load environment variables from .env
load_dotenv()

# Example usage
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

def main():
    # Initialize agents
    pda = ProspectDiscoveryAgent()
    vae = ValidationAgent()
    opa = OutreachPersonalizationAgent()
    cea = CampaignExecutorAgent()

    # Define tools for LangChain
    tools = [
        pda.as_tool(),
        vae.as_tool(),
        opa.as_tool(),
        cea.as_tool(),
    ]

    # Initialize LangChain agent
    llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    # Define a workflow
    query = "CTOs in Berlin SaaS startups"
    workflow = f"""
    Find leads matching the query: {query}.
    Validate their emails and enrich their data.
    Generate personalized messages for each lead.
    Execute an email campaign with the generated messages.
    """

    # Run the workflow
    result = agent.run(workflow)
    print(result)

if __name__ == "__main__":
    main()


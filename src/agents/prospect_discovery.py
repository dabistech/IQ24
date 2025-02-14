import requests
from langchain.agents import Tool
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

class ProspectDiscoveryAgent:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("LINKEDIN_API_KEY")
        self.base_url = "https://api.linkedin.com/v2"

    def find_leads(self, query):
        """
        Simulates querying LinkedIn Sales Navigator for leads based on a search query.
        Example query: "CTOs in Berlin SaaS startups"
        """
        print(f"Searching for leads with query: {query}")

        # Mock API response (replace with real API call when credentials are available)
        mock_data = [
            {"name": "John Doe", "title": "CTO", "company": "StartupX", "industry": "SaaS"},
            {"name": "Jane Smith", "title": "VP of Engineering", "company": "TechCorp", "industry": "AI"},
        ]

        # Simulate filtering based on query
        filtered_leads = [lead for lead in mock_data if query.lower() in f"{lead['title']} {lead['company']} {lead['industry']}".lower()]

        print(f"Found {len(filtered_leads)} leads.")
        return filtered_leads

    def as_tool(self):
        """
        Exposes the agent as a LangChain Tool for integration into workflows.
        """
        return Tool(
            name="ProspectDiscoveryAgent",
            func=self.find_leads,
            description="Finds qualified leads based on a search query."
        )

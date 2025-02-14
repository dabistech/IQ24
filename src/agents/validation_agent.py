import requests

class ValidationAgent:
    def __init__(self, hunter_io_api_key=None):
        self.hunter_io_api_key = hunter_io_api_key or os.getenv("HUNTER_IO_API_KEY")

    def validate_email(self, domain, first_name, last_name):
        """
        Validates email using Hunter.io API.
        """
        url = f"https://api.hunter.io/v2/email-finder?domain={domain}&first_name={first_name}&last_name={last_name}&api_key={self.hunter_io_api_key}"
        response = requests.get(url).json()

        if response.get("data"):
            return response["data"]["email"]
        return None

    def enrich_lead(self, lead):
        """
        Enriches lead data with additional metadata (e.g., company size, industry).
        """
        print(f"Enriching lead: {lead['name']} at {lead['company']}")

        # Mock enrichment data
        enriched_data = {
            "company_size": "51-200 employees",
            "revenue": "$10M-$50M",
            "recent_funding": "Series A ($5M)",
        }

        lead.update(enriched_data)
        return lead

    def as_tool(self):
        """
        Exposes the agent as a LangChain Tool for integration into workflows.
        """
        return Tool(
            name="ValidationAgent",
            func=self.validate_email,
            description="Validates email addresses and enriches lead data."
        )

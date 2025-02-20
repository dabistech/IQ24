from src.agents.outreach_engagement import OutreachEngagementAgent

def main():
    # Initialize agents
    pda = ProspectDiscoveryAgent()
    vae = ValidationAgent()
    opa = OutreachPersonalizationAgent()
    cea = CampaignExecutorAgent()
    afla = AnalyticsAgent()
    cgn = ComplianceAgent()
    oea = OutreachEngagementAgent()

    # Define tools for LangChain
    tools = [
        pda.as_tool(),
        vae.as_tool(),
        opa.as_tool(),
        cea.as_tool(),
        afla.as_tool(),
        cgn.as_tool(),
        oea.as_tool(),
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
    Check compliance of messages.
    Execute an email campaign with the generated messages.
    Engage with prospects on LinkedIn and Twitter.
    Track campaign performance and refine workflows.
    """

    # Run the workflow
    result = agent.run(workflow)
    print(result)

if __name__ == "__main__":
    main()

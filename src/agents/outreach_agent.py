from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

class OutreachPersonalizationAgent:
    def __init__(self, api_key=None):
        self.llm = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))

    def generate_message(self, lead):
        """
        Generates a personalized message for the lead using DeepSeek R1 or GPT.
        """
        prompt_template = PromptTemplate(
            input_variables=["name", "title", "company"],
            template=(
                "Write a highly personalized and professional outreach message "
                "to {name}, who is the {title} at {company}. "
                "The message should focus on how our solution can help their business grow."
            ),
        )

        chain = LLMChain(llm=self.llm, prompt=prompt_template)
        message = chain.run(name=lead["name"], title=lead["title"], company=lead["company"])
        return message

    def as_tool(self):
        """
        Exposes the agent as a LangChain Tool for integration into workflows.
        """
        return Tool(
            name="OutreachPersonalizationAgent",
            func=self.generate_message,
            description="Generates hyper-personalized outreach messages."
        )

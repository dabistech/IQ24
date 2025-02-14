import sendgrid
from sendgrid.helpers.mail import Mail

class CampaignExecutorAgent:
    def __init__(self, sendgrid_api_key=None):
        self.sendgrid_client = sendgrid.SendGridAPIClient(api_key=sendgrid_api_key or os.getenv("SENDGRID_API_KEY"))

    def send_email(self, to_email, subject, message):
        """
        Sends an email via SendGrid.
        """
        mail = Mail(
            from_email="your-email@example.com",
            to_emails=to_email,
            subject=subject,
            html_content=message,
        )
        response = self.sendgrid_client.send(mail)
        return response.status_code

    def as_tool(self):
        """
        Exposes the agent as a LangChain Tool for integration into workflows.
        """
        return Tool(
            name="CampaignExecutorAgent",
            func=self.send_email,
            description="Executes multi-channel campaigns (email, SMS, etc.)."
        )

import requests
from langchain.agents import Tool
from src.utils.logging import log_interaction

class OutreachEngagementAgent:
    def __init__(self, linkedin_api_key=None, twitter_api_key=None):
        self.linkedin_api_key = linkedin_api_key or os.getenv("LINKEDIN_API_KEY")
        self.twitter_api_key = twitter_api_key or os.getenv("TWITTER_API_KEY")

    def send_connection_request(self, platform, prospect, message):
        """
        Sends a personalized connection request or direct message to a prospect.
        """
        if platform.lower() == "linkedin":
            url = f"https://api.linkedin.com/v2/invitation"
            headers = {
                "Authorization": f"Bearer {self.linkedin_api_key}",
                "Content-Type": "application/json",
            }
            payload = {
                "invitee": {"com.linkedin.voyager.growth.invitation.InviteeProfile": prospect["profile_id"]},
                "message": message,
            }
            response = requests.post(url, headers=headers, json=payload)
            log_interaction(platform, "connection_request", prospect, response.status_code)
            return response.status_code

        elif platform.lower() == "twitter":
            url = "https://api.twitter.com/2/dm_conversations/with/:participant_id/messages"
            headers = {
                "Authorization": f"Bearer {self.twitter_api_key}",
                "Content-Type": "application/json",
            }
            payload = {
                "text": message,
                "participant_id": prospect["twitter_id"],
            }
            response = requests.post(url, headers=headers, json=payload)
            log_interaction(platform, "direct_message", prospect, response.status_code)
            return response.status_code

        else:
            raise ValueError(f"Unsupported platform: {platform}")

    def engage_with_post(self, platform, post_id, comment):
        """
        Engages with a prospect's post by liking or commenting.
        """
        if platform.lower() == "linkedin":
            url = f"https://api.linkedin.com/v2/socialActions/{post_id}/comments"
            headers = {
                "Authorization": f"Bearer {self.linkedin_api_key}",
                "Content-Type": "application/json",
            }
            payload = {"comment": comment}
            response = requests.post(url, headers=headers, json=payload)
            log_interaction(platform, "post_comment", {"post_id": post_id}, response.status_code)
            return response.status_code

        elif platform.lower() == "twitter":
            url = "https://api.twitter.com/2/tweets"
            headers = {
                "Authorization": f"Bearer {self.twitter_api_key}",
                "Content-Type": "application/json",
            }
            payload = {"text": comment}
            response = requests.post(url, headers=headers, json=payload)
            log_interaction(platform, "post_comment", {"post_id": post_id}, response.status_code)
            return response.status_code

        else:
            raise ValueError(f"Unsupported platform: {platform}")

    def as_tool(self):
        """
        Exposes the agent as a LangChain Tool for integration into workflows.
        """
        return Tool(
            name="OutreachEngagementAgent",
            func=self.send_connection_request,
            description="Engages with prospects on LinkedIn and Twitter.",
        )

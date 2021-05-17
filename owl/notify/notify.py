import os
import requests
from dotenv import load_dotenv
from owl.notify.message import generate_message

load_dotenv()

URL: str = os.getenv('URL')
API_KEY: str = os.getenv('API_KEY')
CLIENT: str = os.getenv('CLIENT')
RECIPIENT: str = os.getenv('RECIPIENT')
SUBJECT: str = "Owl found a match"


def notify(submission, template: str):
    requests.post(URL,
                  auth=("api", API_KEY),
                  data={"from": CLIENT,
                        "to": RECIPIENT,
                        "subject": SUBJECT,
                        "text": generate_message(submission, template)})

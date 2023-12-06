import os

MAIL_SERVER=os.environ.get("EMAIL_HOST")
MAIL_PORT=os.environ.get("EMAIL_PORT")
MAIL_USERNAME=os.environ.get("EMAIL_USERNAME")
MAIL_PASSWORD=os.environ.get("EMAIL_PASSWORD")
KEY_STRIPE=os.environ.get("KEY_STRIPE")
import os

basedir = os.path.abspath(os.path.dirname(__file__))

MAIL_SERVER=os.getenv("EMAIL_HOST")
MAIL_PORT=os.getenv("EMAIL_PORT")
MAIL_USERNAME=os.getenv("EMAIL_USERNAME")
MAIL_PASSWORD=os.getenv("EMAIL_PASSWORD")
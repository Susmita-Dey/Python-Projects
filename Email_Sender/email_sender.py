# import email
from email.message import EmailMessage
from multiprocessing import context
from dotenv import load_dotenv
import os
import ssl
import smtplib

load_dotenv()

email_sender = 'susmitadey475@gmail.com'
email_password = os.getenv("password")
# print(email_password)
email_receiver = 'jekiw21776@rxcay.com'
subject = "Don't forget to subscribe"
body = '''
When you watch a video, please hit subscribe
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

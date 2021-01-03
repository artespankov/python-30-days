import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


twilio_sid = os.getenv("ACCOUNT_SID")
twilio_secret = os.getenv("TOKEN")
twilio_phone = os.getenv("ACCOUNT_PHONE")

client = Client(twilio_sid, twilio_secret)

sender = twilio_phone
receiver = "+380*********"


txt = "TEST MESSAGE"

# SEND
message = client.messages.create(
    body=txt,
    from_=sender,
    to=receiver
)

# GET DATA
msg_id = message.sid
print(msg_id)
msg_ctx = client.messages.get(msg_id)
msg_instance = msg_ctx.fetch()
print(msg_instance.body)
print(msg_instance.to)
print(msg_instance.from_)

# # LIST
messages = client.messages.list(limit=20, from_=sender)

for i, record in enumerate(messages):
    print(i, record.body, record.from_, record.to)

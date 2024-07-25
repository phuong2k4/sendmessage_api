# Get Api from Twilio
import os
from twilio.rest import Client
SID_Key = os.environ.get("SID")
AUTH_Key = os.environ.get("AUTH")
UrPhone = os.environ.get("MPhone")
TwilioPhone = os.environ.get("TPhone")
# Create client to send message
client = Client(SID_Key, AUTH_Key)
message = client.messages.create(
    body="Send Message Complete",
    from_= TwilioPhone,
    to= UrPhone
)
print(message.status)

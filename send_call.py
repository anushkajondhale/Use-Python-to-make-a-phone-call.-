import os
from twilio.rest import Client

# Load credentials from environment variables
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
recipient_number = os.getenv("RECIPIENT_PHONE_NUMBER")

client = Client(account_sid, auth_token)

# Make the call
call = client.calls.create(
    to=recipient_number,
    from_=twilio_number,
    url="http://demo.twilio.com/docs/voice.xml"  # Twilio provides a demo XML
)

print(f"Call initiated! SID: {call.sid}")

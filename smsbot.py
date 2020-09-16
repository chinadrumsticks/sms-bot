from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "<sid>"
auth_token = "<token>"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+4676999999",
    from_="+199999999999",
    body="Greetings! This is your Python overlord...")

from twilio.rest import Client
from Credentials import account_sid, outh_token, my_cell, my_twilio

client = Client(account_sid, outh_token)

my_msg = ''.join(['I love you\n' for i in range(10)])

message = client.messages.create(to=my_cell, from_=my_twilio,
                                 body=my_msg)
print (message.sid)

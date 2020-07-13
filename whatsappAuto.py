from twilio.rest import Client 
import config
from boto.s3.connection import S3Connection
import os

s3 = S3Connection(os.environ[account_sid], os.environ[auth_token])
 
client = Client(account_sid, auth_token) 


def send_message():
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body='Good Morning!',      
                                  to='whatsapp:+905418396126' 
                              ) 
     
    print(message.sid)

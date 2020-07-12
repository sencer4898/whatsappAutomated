from twilio.rest import Client 
import config
 
account_sid = config.account_sid 
auth_token = config.auth_token
client = Client(account_sid, auth_token) 


def send_message():
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body='Good Morning!',      
                                  to='whatsapp:+905418396126' 
                              ) 
     
    print(message.sid)
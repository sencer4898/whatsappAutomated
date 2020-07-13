from twilio.rest import Client 
import config

account_sid = YOUR_ACCOUNT_SID
auth_token = YOUR_ACCOUNT_TOKEN
 
client = Client(account_sid, auth_token) 


def send_message():
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body='Good Morning!', #Message you want to send     
                                  to='whatsapp:+905418396126' #Person you want to message
                              ) 
     
    print(message.sid)

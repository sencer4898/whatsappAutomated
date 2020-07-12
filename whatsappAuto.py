from twilio.rest import Client 
 
account_sid = 'ACccee6b369575f60d7c1c1f772cecbbb2' 
auth_token = 'c0aad55e7d8ffafba694c4f7bdba23c2' 
client = Client(account_sid, auth_token) 


def send_message():
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body='Good Morning!',      
                                  to='whatsapp:+79818061358' 
                              ) 
     
    print(message.sid)

import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

def send_email(subject,body):
    send_email="ankitbthksyp@gmail.com"
    receiver_email="ankitkashyapbth840@gmail.com"
    password="abmq taju ddzg wahx"
    # google account : manage account
    # search for app-password
    # generate password and use it here
    msg= MIMEMultipart()
    msg["subject"]=subject
    msg["from"]=send_email
    msg["to"]=receiver_email
    
    # add message
    msg.attach(MIMEText(body,"plain"))
    
    filename="app.log"
    with open(filename,'rb') as attachment:
        mime_base=MIMEBase("application","octet-stream")
        mime_base.set_payload(attachment.read())
    
    #Encode file in ASCII for Email
    encoders.encode_base64(mime_base)
    mime_base.add_header("Content-Disposition",f"attachment; filename=bank-statement.log")
    msg.attach(mime_base)
    with smtplib.SMTP("smtp.gmail.com","587") as server:
        server.starttls() # encrypt the connection
        server.login(send_email,password)
        server.send_message(msg)
        print("Message sent successfully!")
        
send_email("BackUp Completed","Backup Created Successfully!")
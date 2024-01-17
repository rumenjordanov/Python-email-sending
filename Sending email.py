import smtplib

sender = "senderEMAIL"
receiver = "recieverEMAIL" 
password = "yourpassword" #read README to see how you get it
subject = "Semi-Auto Python email"
body = "body"

message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587) #change it if you want other mail
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender,receiver,message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")
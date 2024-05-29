import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
#login
server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

with open('password.text', 'r') as f:
    password = f.read()

server.login('examplemail@gmail.com', password)

msg = MIMEMultipart()
msg['from'] = 'Project_Test'
msg['to'] = 'mail@gmail.com'
msg['subject'] = 'Just A Test'

with open('Message.txt.py', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))
#image
filename = 'example.jpg'
attachment = open(filename, 'rb')
#payload
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename{filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('examplemail@gmail.com', 'mail@gmail.com', text)
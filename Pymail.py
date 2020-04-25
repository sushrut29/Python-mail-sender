import smtplib
import imghdr
from email.message import EmailMessage
import config

EMAIL_ADDRESS = config.EMAIL_ADDRESS
EMAIL_PASSWORD = config.PASSWORD

contacts = ['', '']

files = ['1.jpeg','2.jpeg']
# files = ['resumeGFG.pdf']

msg = EmailMessage()
msg['Subject'] = 'Hey! have u received the files?'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
msg.set_content('Image is attached')

for file in files:
	with open(file, 'rb') as f:
		file_data = f.read()
		file_type = imghdr.what(f.name)
		file_name= f.name
	msg.add_attachment(file_data, maintype='image', subtype = file_type, filename= file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg) 

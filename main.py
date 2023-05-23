import smtplib, ssl
import argparse

parser = argparse.ArgumentParser(description='Send mail from python3')
parser.add_argument('--sender', type=str, help='Sender email address')
parser.add_argument('--receiver', type=str, help='Receiver email address')
parser.add_argument('--subject', type=str, help='Subject of the email')
parser.add_argument('--body', type=str, help='Body of the email')
parser.add_argument('--password', type=str, help='Password of the sender email address')
parser.add_argument('--port', type=int, help='Port number of the sender email address')
parser.add_argument('--smtp', type=str, help='SMTP server address')
args = parser.parse_args()

if args.sender:
    sender = args.sender
else:
    sender = input('Enter sender email address: ')
if args.password:
    password = args.password
else:
    password = input('Enter password: ')
if args.receiver:
    receiver = args.receiver
else:
    receiver = input('Enter receiver email address: ')
if args.subject:
    subject = args.subject
else:
    subject = input('Enter subject: ')
if args.body:
    body = args.body
else:
    body = input('Enter body: ')
if args.port:
    port = args.port
else:
    port = 465
    print('Port number not provided, using default port number 465')
if args.smtp:
    smtp = args.smtp
else:
    smtp = 'smtp.gmail.com'
    print('SMTP server address not provided, using default smtp server address smtp.gmail.com')

message = '''\
Subject: {subject}

{body}
'''.format(subject=subject, body=body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host=smtp, port=port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
    print('Mail sent successfully')

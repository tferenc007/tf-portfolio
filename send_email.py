import smtplib, ssl

host = "smtp.gmail.com"
port = 465

context = ssl.create_default_context()

def send_email(message):
    username='app.tferenc@gmail.com'
    password = 'hhup hkxl datz fwgt'

    reciver ="ferenc.tomasz007@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login (username, password)
        server.sendmail(username,reciver, message)

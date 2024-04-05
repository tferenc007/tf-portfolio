import smtplib, ssl

host = "smtp.gamil.com"
port = 465


def send_email(message):
    username='app.tferenc@gmail.com'
    password = 'Asdkfgdfs93784927LKJ'

    reciver ="ferenc.tomasz007@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login (username, password)
        server.sendmail(username,reciver, message)

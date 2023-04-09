import smtplib

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mayankforspotify@gmail.com', 'mayank22kirola06')
    server.sendmail('mayankforspotify@gmail.com', to, content)
    server.close()

def es(to,content):
    try:   
        sendEmail(to, content)
        n="Email has been sent!"

    except Exception as e:
        n="Sorry . I am not able to send this email"

    return n

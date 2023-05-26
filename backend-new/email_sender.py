import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    print(sender_email, sender_password, recipient_email)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    try:
        server.login(sender_email, sender_password)
        server.send_message(msg)
    except Exception as e:
        raise Exception(f'An error occurred while sending the email: " {str(e)}')
    finally:
        server.quit()


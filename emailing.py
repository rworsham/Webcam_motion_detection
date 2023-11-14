import smtplib
import ssl
import os
from email.message import EmailMessage
import imghdr


password = os.getenv("PASSWORD")
def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "!Motion Detected!"
    email_message.set_content("Motion detected in X room")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content,
                                 maintype="image", subtype=imghdr.what(None, content))
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login("worshamappmanager@gmail.com", password)
    gmail.sendmail("worshamappmanager@gmail.com"
                   ,"robertworsham01@gmail.com"
                   , email_message.as_string())
    print("send_email function ended")

if __name__ == "__main__":
    send_email()




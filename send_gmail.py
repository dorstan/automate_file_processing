#!/usr/bin/env python3
from email.message import EmailMessage
import smtplib
import os, sys
import os.path
import mimetypes
import getpass


def generate_email (sender, recipient, subject, body, attachement_path=None):
    """This function creates an email and returns a variable called <message> containing a recipient or recipients list with attachement if needed."""
    
    if isinstance(recipient, list):
        contacts = ", ".join(recipient)
    else:
        contacts = recipient

    message = EmailMessage()
    message["From"] = sender
    message["To"] = contacts
    message["Subject"] = subject
    message.set_content(body)

    # These lines make the attachement optional.
    if attachement_path != None:
        for attached_file in os.listdir(attachement_path):
            path_file = os.path.join(attachement_path, attached_file)
            mime_type, _ = mimetypes.guess_type(attached_file)
            mime_type, mime_subtype = mime_type.split("/", 1)

            with open (path_file, "rb") as pf:
                message.add_attachment(
                    pf.read(),
                    maintype = mime_type,
                    subtype = mime_subtype,
                    filename = attached_file
                )
    return message

def send_email(message):
    """This function sends the message to the configured SMTP_SSL gmail server."""
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as mail_server:
        mail_pass = getpass.getpass("Password? ")
        sender = message["From"]
        mail_server.login(sender, mail_pass)
        mail_server.send_message(message)


if __name__ == "__main__":
    mail_template = sys.argv[1]
    with open (mail_template, "r") as mt:
            mail_sender = mt.readline().strip("\n").replace("Sender: ", "")
            mail_recipient = mt.readline().strip("\n").replace("Recipient: ", "")
            mail_subject = mt.readline().strip("\n").replace("Subject: ", "")
            mail_body = mt.readline().strip("\n").replace("Body: ", "")
            mail_attachement_path = mt.readline().strip("\n").replace("Attachements: ", "")

    if mail_attachement_path == "":
        mail_attachement_path = None


    create_mail = generate_email(
        sender = mail_sender,
        recipient=mail_recipient,
        subject=mail_subject,
        body=mail_body,
        attachement_path=mail_attachement_path
    )
    send_email(create_mail)




#!/usr/bin/env python3
from email.message import EmailMessage
import smtplib
import os
import os.path
import mimetypes
import getpass


message = EmailMessage()
attachement_path = "~/Kode/email_config/picture_mail"
sender = "dorin.grigore.stanchescu@gmail.com"
contacts = ["stanchescudorin@gmail.com", "stanchescuroxana@gmail.com"]
subject = "Files automation"
body = """
Dear all,
These are some files.
Kr,
DSG
"""

message["From"]=sender
message["To"]= ", ".join(contacts)
message["Subject"] = subject
message.set_content(body)

for file in os.listdir(attachement_path):
    path_file = os.path.join(attachement_path, file)
    mime_type, _ = mimetypes.guess_type(file)
    mime_type, mime_subtype = mime_type.split("/", 1)
    with open (path_file, "rb") as atp:
        message.add_attachment(
            atp.read(),
            maintype=mime_type, 
            subtype=mime_subtype, 
            filename=file
        )
with smtplib.SMTP_SSL("smtp.gmail.com",465) as mail_server:
    mail_pass = getpass.getpass("Password? ")
    mail_server.login(sender, mail_pass)
    mail_server.send_message(message)

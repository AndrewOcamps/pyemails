
# Gerardo Ocampos 15/02/2020

import email.message
import mimetypes
import os.path
import smtplib

def generate(sender, recipient, subject, body, attachment_path=False):
    """
    This function receives 4 mandatory and 1 optional arguments
    Example:
    >> mandatory:
        sender = gerardo.ocampos
        recipient = juan.perez
        subject = 'A simple subject'
        body = 'content of the mail'
    >> optional:
        attachment_path = '/tmp/example.pdf'

    generate('gerardo.ocampos','juan.perez','A simple subject', 'content of the mail', '/tmo/example.pdf')

    RETURN:
    message object

    """
    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    if attachment_path:
        attachment_file = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/',1)

        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(),
                                    maintype=mime_type,
                                    subtype=mime_subtype,
                                    filename=attachment_file)

    return message


def send(message, server='localhost'):
    mail_server = smtplib.SMTP(server)
    mail_server.send_message(message)
    mail_server.quit()

    


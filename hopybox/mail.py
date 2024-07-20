import os
import smtplib

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from .prompt import getpass
from .prompt import tip_tick
from .prompt import error_cross
from .prompt import color_print
from .prompt import color_input


def email_send_pro_system(user, password, host, to, subject, body, attachments):
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))
    if attachments:
        attachment = open(attachments, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',f'Attachment;filename={os.path.basename(attachments)}')
        msg.attach(part)
    with smtplib.SMTP_SSL(host, 465) as smtp:
        smtp.login(user, password)
        smtp.sendmail(user, to, msg.as_string())


def email():
    user = color_input('Your Email Address\n','#5C5CFF')
    to = color_input('Receive Email Address\n','#5C5CFF')
    password = getpass('Email Authorization Code\n','#00FF00')
    host = color_input('Emailbox Server Address\n','#00FF00')
    subject = input('Email Title\n','#00FF00')
    body = input('Email Text Contents\n','#00FF00')
    attachments = input('Email Attachments (Wrap To Skip)\n','#00FFFF')
    if not attachments:
        attachments = None
    email_send_pro_system(user, password, host, to, subject, body, attachments)
    tip_tick('Email sent successfully')

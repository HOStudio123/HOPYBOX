import os
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from .prompt import getpass
from .prompt import tip_tick
from .prompt import error_cross

def email_send_pro_system(user,password,host,to,subject,body,attachments):
  msg = MIMEMultipart()
  msg['From'] = user
  msg['To'] = to
  msg['Subject'] = subject
  msg.attach(MIMEText(body,'plain'))
  if attachments:
    attachment = open(attachments,'rb')
    part = MIMEBase('application','octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',f"Attachment;filename={os.path.basename(attachments)}")
    msg.attach(part)
  with smtplib.SMTP_SSL(host,465) as smtp:
    smtp.login(user,password)
    smtp.sendmail(user,to,msg.as_string())

def email():
  user = input('\033[94mYour Email Address\n\033[0m')
  to = input('\033[94mReceive Email Address\n\033[0m')
  password = getpass('Email Authorization Code\n','magenta')
  host = input('\033[92mEmailbox Server Address\n\033[0m')
  subject = input('\033[92mEmail Title\n\033[0m')
  body = input('\033[92mEmail Text Contents\n\033[0m')
  attachments = input('\033[96mEmail Attachments (Wrap To Skip)\n\033[0m')
  if not attachments:
    attachments = None
  email_send_pro_system(user,password,host,to,subject,body,attachments)
  tip_tick('Email sent successfully')
import yagmail
from getpass import getpass
from .prompt import error_cross

def email(to_email):
  user = input('\033[1;94mYour Email Address:\n\033[0m')
  password = getpass('\033[1;95mEmail Authorization Code:\n\033[0m')
  host = input('\033[1;92mEmailbox Server Address:\n\033[0m')
  to = to_email
  subject = input('\033[1;92mEmail Title:\n\033[0m')
  contents = input('\033[1;92mEmail Text Contents:\n\033[0m')
  attachments = input('\033[1;92mEmail Attachments:(Wrap To Skip)\n\033[0m')
  print(attachments)
  if not attachments:
    attachments = None
  try:
    yag = yagmail.SMTP(user=user,password=password,host=host)
    yag.send(to=to,subject=subject,contents=contents,attachments=attachments)
  except:
    error_cross('SendEmailError','Command','Error sending the message',f'email {to_email}')
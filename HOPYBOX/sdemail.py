import yagmail
import getpass
from .hopter import Error_pta
def text_email(to_email,title,text,email_password,user_email,host_email):
  user = user_email
  password = email_password
  host = host_email
  to = [to_email]
  subject = title
  contents = [text]
  yag = yagmail.SMTP(user=user, password=password, host=host)
  yag.send(to=to, subject=subject, contents=contents)
def sd_email(to_email):
  user = input('\033[92mThe mailbox where the mail will be sent ? \033[0m')
  password = getpass.getpass('\033[92mEmail authorization code of the email to be sent ? \033[0m')
  host = input('\033[92mMailbox server address ? \033[0m')
  to = to_email
  title = input('\033[92mMail title ? \033[0m')
  text = input('\033[92mMail text ? \033[0m')
  try:
    text_email(to,title,text,password,user,host)
  except:
    Error_pta('SendEmailError','Command','Error sending the message','email '+to_email)
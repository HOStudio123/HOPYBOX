import pyotp
import random
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import scrypt
from .prompt import getpass
from .prompt import tip_tick
from .prompt import error_cross
from .prompt import ask_proceed

def encipher(password,plaintext):
  salt = get_random_bytes(AES.block_size)
  key = scrypt(password, salt, AES.block_size, N=2**14, r=8, p=1)
  cipher = AES.new(key, AES.MODE_GCM)
  ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
  return b64encode(salt+cipher.nonce+ciphertext+tag).decode()

def decrypt(password,encrypted_text):
  encrypted_data = b64decode(encrypted_text.encode())
  salt = encrypted_data[:AES.block_size]
  nonce = encrypted_data[AES.block_size:AES.block_size+AES.block_size]
  ciphertext = encrypted_data[AES.block_size+AES.block_size:-AES.block_size]
  tag = encrypted_data[-AES.block_size:]
  key = scrypt(password, salt, AES.block_size,N=2**14,r=8,p=1)
  cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
  plaintext = cipher.decrypt_and_verify(ciphertext,tag)
  return plaintext.decode()

class Totp:
  def set(self):
    name = input('\033[95mServes Name\n\033[0m')
    password = f"{random.randint(1,999999):06d}"
    secret = encipher(password,getpass('\033[92mTOTP Secret Key\n\033[0m'))
    with open('.totp_password.hpb','a+') as f:
      print(f'{name} {password} {secret}',file=f)
    tip_tick("Succeeded in setting")
  def display(self):
    with open('.totp_password.hpb','r') as f:
      for line in f.readlines():
        otp = self.switch(decrypt(line.split(' ')[1],line.split(' ')[2]))
        print(f"\033[92m[{line.split(' ')[0]}]\033[0m\033[97m {otp}")
  def switch(self,secret):
    return pyotp.TOTP(secret).now()
  def delete(self):
    i = 0
    with open('.totp_password.hpb','r') as f:
      lines = f.readlines()
      for line in lines:
        i+=1
        print(f"\033[92m[{i}]\033[0m\033[97m {line.split(' ')[0]}")
    if lines:
      line = int(input("\033[0m\033[95mWhich 2FA service do you want to delete ? \033[0m"))
      if 0 < line <= len(lines):
        while True:
          result = ask_proceed("Do you really want to permanently delete this 2FA service ?")
          if result == True:
            del lines[line-1]
            with open('.totp_password.hpb','w') as f:
              f.writelines(lines)
            tip_tick('Successfully deleted')
            break
          elif result == None:
            continue
          else:
            break
      else:
        error_cross('SericalNumberError','Program','This serial number cannot be found',line)
    else:
      error_cross('KeyNotFoundError','Program','No TOTP key was found',lines)
        
    
totp = Totp()
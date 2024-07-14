#!/usr/bin/env python3

# -*- coding:utf-8 -*-

'''
Copyright (c) 2022-2024 HOStudio123(ChenJinlin).
All Rights Reserved.
'''

import os
import hmac
import time
import pyotp
import base64
import pickle
import hashlib
import sqlite3

from cryptography.fernet import Fernet as fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

from .prompt import getpass
from .prompt import tip_tick
from .prompt import ask_proceed
from .prompt import error_cross_simple

from .timetool import timetool

default = os.path.join(os.path.expanduser('~'),'.hopybox')

class Cipher:
  def __init__(self,message):
    self.message = message
  @property
  def en_sha256(self):
    h = hashlib.new('sha256')
    h.update(bytes(self.message,encoding='utf-8'))
    return h.hexdigest()
  @property
  def en_sha512(self):
    h = hashlib.new('sha512')
    h.update(bytes(self.message,encoding='utf-8'))
    return h.hexdigest()
  @property
  def en_md5(self):
    h = hashlib.new('md5')
    h.update(bytes(self.message,encoding='utf-8'))
    return h.hexdigest()
  @property
  def en_base64(self):
    digest = hashes.Hash(hashes.SHA256(),backend=default_backend())
    digest.update(self.message.encode())
    return base64.urlsafe_b64encode(digest.finalize())
  def en_fernet(self,key):
    fer = fernet(key)
    return fer.encrypt(self.message.encode()).decode('utf-8')
  def de_fernet(self,key):
    fer = fernet(key)
    return fer.decrypt(self.message.encode()).decode('utf-8')

cipher = Cipher

class Two_factor:
  def __init__(self,path=default):
     self.db_path = os.path.join(default,'two_factor.db')
     self.dat_path = os.path.join(default,'two_factor.dat')
     if not os.path.exists(self.db_path):
       self.con = sqlite3.connect(self.db_path)
       self.cur = self.con.cursor()
       self.cur.execute('CREATE TABLE TF (time,server,account,key)')
     else:
       self.con = sqlite3.connect(self.db_path)
       self.cur = self.con.cursor()
  def add(self,data):
    self.cur.execute('INSERT INTO TF (time,server,account,key) VALUES (?,?,?,?)',data)
    self.con.commit()
    del data
  @property
  def load(self):
    return self.cur.execute("SELECT * FROM TF").fetchall()
  def delete(self,data):
    self.cur.execute("DELETE FROM TF WHERE time = '(?)'")
    self.con.commit()
  def pin_set(self,value):
    with open(self.dat_path,'wb') as f:
      pickle.dump(value,f)
  @property
  def pin_load(self):
    with open(self.dat_path,'rb') as f:
      return pickle.load(f)
  def pin_verify(self,pin):
    return hmac.compare_digest(cipher(pin).en_sha256,self.pin_load)
  @property
  def _set_pin(self):
    if not os.path.isfile(self.dat_path):
      pin = getpass('Please set the PIN code (at least 6 digits)\n','green')
      if len(pin)>=6:
        self.pin_set(cipher(pin).en_sha256)
        tip_tick('Succeeded in setting the PIN code, please remember this PIN code well, which cannot be reset')
      else:
        error_cross_simple('This is an unreasonable input')
    else:
      error_cross_simple('You already set it up')
  @property
  def _verify_pin(self):
    pin = getpass('Please enter the PIN code\n','green')
    return self.pin_verify(pin)
  @property
  def _add_factor(self):
    if not os.path.isfile(self.dat_path):
      self._set_pin()
    server = input('\033[95mServes Name\n\033[0m')
    account = input('\033[95mAccount name\n\033[0m')
    timestamp = int(time.time())
    key = cipher(self.pin_load).en_base64
    token = cipher(getpass('Secret Key\n','green')).en_fernet(key)
    data = (timestamp,server,account,token)
    self.add(data)
    tip_tick('Succeeded in setting the two-factor')
  def otp_pro(self,secret):
    return pyotp.TOTP(secret).now()
  @property
  def _output(self):
    data = self.load
    if self._verify_pin:
      if len(data)==0:
        error_cross_simple("It's empty")
      for i in data:
        try:
          key = cipher(self.pin_load).en_base64
          otp = self.otp_pro(cipher(i[3]).de_fernet(key))
          del key
        except Exception as e:
          print(e)
          otp = '(Worng Formatting)'
        finally:
          print(f'\033[92m[{i[1]}] \033[94m({i[2]}) \033[97m{otp}')
    else:
      error_cross_simple('The entered PIN code is incorrect')
  @property
  def _delete(self):
    data = self.load
    i = 0
    link = list()
    if len(data)==0:
        error_cross_simple("It's empty")
    else:
      for j in data:
        i+=1
        c_time = timetool.ymd_hms_format(j[0])
        print(f'\033[96m[{i}] \033[95m[{c_time}] \033[92m[{j[1]}] \033[94m({j[2]})\033[0m')
        link.append(j[0])
      line = int(input('\033[97mWhich two-factor do you want to delete ? \033[0m'))
      if 0 < line <= len(data):
        while True:
          result = ask_proceed("Do you really want to permanently delete this two-factor ?")
          if result == True:
            self.delete(link[i-1])
            tip_tick('Successfully deleted the two-factor')
            break
          elif result == None:
            continue
          else:
            break
      else:
        error_cross_simple('This is an unreasonable input')

two_factor = Two_factor()
import os
import time
import hmac
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
from .prompt import color_print
from .prompt import color_input

from .timetool import timetool

default = os.path.join(os.path.expanduser('~'),'.config','hopybox')


class Cipher:
    def __init__(self, message):
        self.message = message

    @property
    def en_sha256(self):
        h = hashlib.new('sha256')
        h.update(bytes(self.message, encoding='utf-8'))
        return h.hexdigest()

    @property
    def en_sha512(self):
        h = hashlib.new('sha512')
        h.update(bytes(self.message, encoding='utf-8'))
        return h.hexdigest()

    @property
    def en_md5(self):
        h = hashlib.new('md5')
        h.update(bytes(self.message, encoding='utf-8'))
        return h.hexdigest()

    @property
    def en_base64(self):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(self.message.encode())
        return base64.urlsafe_b64encode(digest.finalize())

    def en_fernet(self, key):
        fer = fernet(key)
        return fer.encrypt(self.message.encode()).decode('utf-8')

    def de_fernet(self, key):
        fer = fernet(key)
        return fer.decrypt(self.message.encode()).decode('utf-8')


cipher = Cipher


class Two_factor:
    def __init__(self, path=default):
        self.dat_path = os.path.join(default,'two_factor.dat')
        self.db_path = os.path.join(default,'two_factor.db')
        self.con = sqlite3.connect(self.db_path)
        self.cur = self.con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS TF (time,server,account,key)')
        
    @property
    def load(self):
        return self.cur.execute('SELECT * FROM TF').fetchall()

    def add(self, data):
        self.cur.execute('INSERT INTO TF (time,server,account,key) VALUES (?,?,?,?)', data)
        self.con.commit()

    def delete(self, data):
        self.cur.execute(f'DELETE FROM TF WHERE time = {data}')
        self.con.commit()
    
    @property       
    def detect_pin_set(self):
        if os.path.isfile(self.dat_path):
            return True
        else:
            return None  
    @property
    def pin_load(self,):
        with open(self.dat_path, 'rb') as f:   
            return pickle.load(f)
   
    def pin_set(self,value):
         with open(self.dat_path, 'wb') as f:
             pickle.dump(value,f)
            
    def pin_verify(self,pin):
         return [hmac.compare_digest(cipher(pin).en_sha256,self.pin_load),cipher(pin).en_sha512]

    @property
    def _set_pin(self):
        if not self.detect_pin_set:
            while True:
                pin = getpass('Please set the PIN code (at least 6 digits)\n','#00FF00')
                if len(pin) >= 6:
                    self.pin_set(cipher(pin).en_sha256)
                    del pin
                    tip_tick('Succeeded in setting the PIN code, please remember this PIN code well, which cannot be reset')
                    break
                else:
                    error_cross_simple('This is an unreasonable input')
        else:
            error_cross_simple('You already set it up')

    @property
    def _verify_pin(self):
        pin = getpass('Please enter the PIN code\n','#00FF00')
        return self.pin_verify(pin)

    @property
    def _add_factor(self):
        if not self.detect_pin_set:
            self._set_pin
        server = color_input('Serves Name\n','#FF00FF')
        account = color_input('Account name\n','#FF00FF')
        timestamp = int(time.time())
        pin_key = self._verify_pin
        if pin_key[0]:
            token = self.otp_verify(getpass('Secret Key\n','#00FF00'),pin_key[1])
            del pin_key
            if token:
                data = (timestamp, server, account, token)
                self.add(data)
                tip_tick('Succeeded in setting the two-factor')
            else:
                error_cross_simple('This is an unreasonable input')
        else:
            error_cross_simple('The entered PIN code is incorrect')

    def otp_pro(self, secret):
        return pyotp.TOTP(secret).now()
    
    def otp_verify(self, secret, key):
        try:
            self.otp_pro(secret)
            token = cipher(secret).en_fernet(cipher(key).en_base64)
            del secret,key
            return token
        except:
            return None

    @property
    def _output(self):
        data = self.load
        pin_key = self._verify_pin
        if pin_key[0]:
            if len(data) == 0:
                del pin_key
                error_cross_simple("It's empty")
            for i in data:
                otp = self.otp_pro(cipher(i[3]).de_fernet(cipher(pin_key[1]).en_base64))
                text = [
                ('class:server',f'[{i[1]}]'),
                ('',' '),
                ('class:account',f'[{i[2]}]'),
                ('',' '),
                ('class:otp',otp)
                ]
                style = {
                'server':'#00FF00',
                'account':'#5C5CFF',
                'otp':'#FFFFFF'
                }
                color_print(text,style,single=False)
            del pin_key
        else:
            error_cross_simple('The entered PIN code is incorrect')

    @property
    def _delete(self):
        data = self.load
        i = 0
        link = list()
        if len(data) == 0:
            error_cross_simple("It's empty")
        else:
            for j in data:
                i += 1
                c_time = timetool.ymd_hms_format(j[0])
                text = [
                ('class:line',f'[{i}]'),
                ('',' '),
                ('class:time',f'[{c_time}]'),
                ('',' '),
                ('class:server',f'[{j[1]}]'),
                ('',' '),
                ('class:account',f'({j[2]})')
                ]
                style = {
                'line':'#00FFFF',
                'time':'#FF00FF',
                'server':'#00FF00',
                'account':'#5C5CFF'
                }
                color_print(text,style,single=False)
                link.append(j[0])
            line = int(color_input('Which two-factor do you want to delete ? ','#FFFFFF'))
            if 0 < line <= len(data):
                result = ask_proceed('Do you really want to permanently delete this two-factor ?')
                if result:
                    self.delete(link[line-1])
                    tip_tick('Successfully deleted the two-factor')
            else:
                error_cross_simple('This is an unreasonable input')


two_factor = Two_factor()

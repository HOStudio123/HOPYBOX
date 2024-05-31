import os
import sys
import time
import uuid
import json
import locale
import socket
import psutil
import datetime
import requests
import platform
# from .headers import headers_water

class Device:
  def name(self):
    return platform.node()
  def type(self):
    return platform.machine()
  class Web:
    class IP:
      def local(self):
        return socket.gethostbyname(socket.gethostname())
      def public(self):
        return requests.get('https://api.ipify.org').text
    def hostname(self):
      return socket.gethostname()
    def mac(self):
      mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
      return ":".join([mac[e:e+2] for e in range(0,11,2)])
  class System:
    def name(self):
      return platform.system()
    def version(self):
      return platform.platform()
    def language(self):
      return locale.getlocale()[0]
    def encode(self):
      return locale.getlocale()[1]
  class Processor:
    def type(self):
      return platform.processor()
    def logic_count(self):
      return psutil.cpu_count()
    def core_count(self):
      return psutil.cpu_count(logical=False)
  class Memory:
    def total(self):
      return f'{float(psutil.virtual_memory().total)/1024**3:.2f}GB'
    def used(self):
      return f'{float(psutil.virtual_memory().used)/1024**3:.2f}GB'
    def free(self):
      return f'{float(psutil.virtual_memory().free)/1024**3:.2f}GB'
    def percent(self):
      return f'{str(int(round(psutil.virtual_memory().percent)))}%'
  class Storage:
    def total(self,path):
      storage = psutil.disk_usage(path)
      return f'{storage.total/(1024**3):.2f}GB'
    def used(self,path):
      storage = psutil.disk_usage(path)
      return f'{storage.used/(1024**3):.2f}GB'
    def free(self,path):
      storage = psutil.disk_usage(path)
      return f'{storage.free/(1024**3):.2f}GB'
    def percent(self,path):
      storage = psutil.disk_usage(path)
      return f'{storage.percent}%'
  class Fps():
    def fps(self):
      start_time = time.time()
      end_time = 0
      fps = 0
      while not end_time-start_time >= 1:
        fps+=1
        end_time = time.time()
      return fps
  class Time():
     def timestamp(self):
       return time.time()
     def time_local(self):
       return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       
device = Device()
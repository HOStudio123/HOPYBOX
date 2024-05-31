import os
import re

def terminal(command):
  os.system(command)

def clear():
  terminal('clear')

def char(text):
  pat_en = re.compile(r'^[a-zA-Z]+$')
  pat_cn = re.compile(r'^[\u4e00-\u9fff]+$')
  if bool(pat_en.match(text)):
    return ['en','zh-CN']
  elif bool(pat_cn.match(text)):
    return ['zh-CN','en']
  else:
    return None
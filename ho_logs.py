import os
import time
from ho_version import *
open_time = time.mktime(time.localtime(time.time()))
try:
  os.mkdir('/storage/emulated/0/._PyDroid/HOPYBOX/logs/')
except Exception:
  pass
with open('/storage/emulated/0/._PyDroid/HOPYBOX/logs/{}.log'.format(open_time),'a+') as _file:
  _file.write(ho_version+'\n')
def wlog(text,returns):
  mtime = time.localtime(time.mktime(time.localtime(time.time())))
  mtime = time.strftime("%Y/%m/%d %H:%M:%S",mtime)
  ho_logs = open('/storage/emulated/0/._PyDroid/HOPYBOX/logs/{}.log'.format(open_time),'a+')
  ho_logs.write('\n[{}]\n├ INPUT:{}\n└ RETURN:\n{}'.format(mtime,text,returns))
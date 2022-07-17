'''
            Copyright (c) 2022 HOStudio123(ChenJinlin) ,
                      All Rights Reserved.
'''
from platform import python_version
from .hopter import Error_ptc
from rich.console import Console
from time import sleep
import os
python_code = python_version().split('.')
console = Console()
if int(python_code[0]) < 3:
  print('E:Sorry, You python version is less than 3.8, and this program cannot be used.')
elif int(python_code[1]) < 8:
  print('E:Sorry, You python version is less than 3.8, and this procedure cannot be used.')
else:
  try:
    from .__main__ import *
  except Exception as e:
    Error_ptc('Sorry,The program has an error and cannot continue to run',str(e))
    print('\033[93mWARNING:The process is about to automatically restart … 3',end='\r')
    sleep(1)
    print('\033[93mWARNING:The process is about to automatically restart … 2',end='\r')
    sleep(1)
    print('\033[93mWARNING:The process is about to automatically restart … 1',end='\r')
    sleep(1)
    print('\033[93mWARNING:The process is about to automatically restart … 0',end='\r')
    console.clear()
    os.system('python3 -m hopybox')
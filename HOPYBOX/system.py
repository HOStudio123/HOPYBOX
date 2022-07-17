import os,pip
import requests as visit
from .hopter import Error_pta
from .headers import headers_water
from .LICENSE import license_print
from .helps import helps_print
from .copyright import copyright_print
from rich.console import Console
from rich.traceback import install

install(show_locals=True)
console = Console()
headers = headers_water()

def systems(order):
  print('\033[96m',end='\r')
  os.system(order)

def runpy(module):
  print('\033[0m',end='\r')
  os.system('python3 '+module)

def python():
  os.system('python3')

def install(modules):
  print('\033[96m',end='\r')
  os.system('python3 -m pip install -U {}'.format(modules))

def uninstall(modules):
  print('\033[96m',end='\r')
  os.system('python3 -m pip uninstall {}'.format(modules))

def all_help():
  print(helps_print())

def license():
  print('\033[96m'+license_print())

def copyright():
  print('\033[96m'+copyright_print())

def module_help(module):
  print('\033[96m'+str(help(module)))
  
def pip_list():
  print('\033[96m',end='\r')
  os.system('pip list')

def clear_text():
  console.clear()

def update_tip():
  print('\033[96mEnter update(version number) to get a changelog about the version object')

def debug(command):
  try:
    print(eval(command))
  except Exception as e:
    Error_pta('DebugError','Command',str(e),'debug '+command)

def ipython():
  os.system('ipython')
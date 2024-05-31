import os
import requests as visit
from rich.console import Console
from .prompt import tip_tick,tip_arrow,error_cross

console = Console()

def terminal(command):
  os.system(command)

def run_py(file):
  terminal(f'python3 {file}')

def python():
  terminal('python3')

def install(module):
  terminal(f'python3 -m pip install -U {module}')

def uninstall(module):
  terminal(f'python3 -m pip uninstall {module}')

def module_help(module):
  help(module)

def clear_text():
  console.clear()
  
def this():
  print('''\033[96mThe Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!''')

def debug(command):
  try:
    eval(command)
  except Exception as e:
    error_cross('DebugError','Command',str(e),f'debug {command}')


    
import os
import time
import chardet
import webbrowser
import requests
from rich import syntax
from rich.console import Console
from bs4 import BeautifulSoup as soup
from .headers import headers_water
from .prompt import tip_tick
from .prompt import error_cross

# Disable Security Request Warning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3.exceptions import InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

console = Console()
headers = headers_water()

class Choget:
  def __init__(self):
    pass
  def time(self,state):
    if state:
      start_time = time.time()
    else:
      return time.time() - start_time
    
    
def hoget(url):
  global headers
  start_time = time.time()
  try:
    with Console().status("\033[96mLoading URL …"):
      res = requests.get(url,headers=headers,stream=True,verify=False)
    if res.status_code == 200:
      end_time = time.time()
      total_time = end_time - start_time
      print('\033[32mURL-URL:\033[0m\033[94m\n'+res.url) 
      print('\033[32mURL-Time:\033[0m\033[94m\n'+str(total_time)+'S')
      with Console().status("\033[96mLoading information …"):
        print('\033[32mURL-Szie:\033[0m\033[94m\n'+str(len(res.text))+'B')
      print('\033[32mURL-Cookies:\033[0m\033[94m')
      for name, value in requests.utils.dict_from_cookiejar(res.cookies).items():
        print('* %s:%s ' % (name, value))
      if not requests.utils.dict_from_cookiejar(res.cookies):
        print(None)
      print('\033[32mURL-Headers:\033[0m\033[94m')
      for name, value in res.headers.items():
        print('* %s:%s ' % (name, value))
      print('\033[32mURL-Requests-Headers:\033[0m\033[94m')
      for name, value in res.request.headers.items():
        print('* %s:%s ' % (name, value))
      print(f'\033[92mURL-Code-Coding:\033[0m\033[94m\n{res.encoding}')
      if res.encoding != None:
        print('\033[92mURL-Code-Type:\033[0m\033[94m\nGeneral network\033[0m')
        print()
        res.encoding = chardet.detect(res.content)['encoding']
        print('\033[92mURL-Code-Content:\033[0m')
        console.print(syntax.Syntax(res.text,'html',theme="ansi_dark", line_numbers=True))
      else:
        print('\033[92mURL-Code-Type:\033[0m\033[94m\nOther network\033[0m')
        print('\033[92mURL-Code-Content:\033[0m')
        console.print(syntax.Syntax(str(res.text),'html',theme='ansi_dark', line_numbers=True))
    else:
      error_cross(f'{res.status_code} Error','Command',f'{res.status_code} Error in request',f'hoget {url}')
  except Exception as e:
    error_cross(e.__class__.__name__,'Command',e,f'hoget {url}')
    
def browser(url):
  try:
    webbrowser.open(url) 
    tip_tick('The program has opened the URL in the browser')
  except Exception as e:
    error_cross('OpenBrowserError','Command',e,f'browget {url}')
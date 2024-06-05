import os
import time
import webbrowser
import requests
from rich import syntax
from rich.console import Console
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

class Hoget:
  def __init__(self):
    self.start_time = 0
    self.total_time = 0
  def main(self,url):
    self.time(True)
    with Console().status("\033[96mLoading URL …"):
      res = self.content(url)
    if res.status_code == requests.codes.ok:
      self.total_time = self.time(False)
      print(f"\033[32mUniform Resource Locator\033[0m\033[95m\n{res.url}\n\033[32mRequest Duration\033[0m\033[95m\n{self.total_time} s")
      with Console().status("\033[96mLoading information …"):
        cache = res.content
        print(f"\033[32mWebsite Size\033[0m\033[95m\n{len(cache)} B")
        print('\033[32mHeaders\033[0m\033[95m')
        for name, value in res.headers.items():
          print('* %s:%s ' % (name, value))
        print('\033[32mRequests Headers\033[0m\033[95m')
        for name, value in res.request.headers.items():
          print('* %s:%s ' % (name, value))
        print('\033[32mCookies\033[0m\033[95m')
        for name, value in requests.utils.dict_from_cookiejar(res.cookies).items():
          print('* %s:%s ' % (name, value))
        if not requests.utils.dict_from_cookiejar(res.cookies):
          print('None')
        print(f'\033[32mEncoding\033[0m\033[95m\n{res.encoding}')
      print('\033[32mContent\033[0m')
      if res.encoding:
        self.content_out(cache.decode(res.encoding))
      else:
        print(cache)
    else:
      error_cross(f'{res.status_code} Error','Command',f'{res.status_code} Error in request',f'hoget {url}')
  def time(self,state):
    if state:
      self.start_time = time.time()
    else:
      return time.time() - self.start_time
  def content(self,url):
    return requests.get(url,headers=headers,stream=True,verify=False)
  def content_out(self,content):
    console.print(syntax.Syntax(content,'html',theme="ansi_dark",line_numbers=True))
    
def browser(url):
  try:
    webbrowser.open(url) 
    tip_tick('The program has opened the URL in the browser')
  except Exception as e:
    error_cross('OpenBrowserError','Command',e,f'browget {url}')

hoget = Hoget()
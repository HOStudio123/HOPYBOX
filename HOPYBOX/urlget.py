import os
import time
import chardet
import requests as visit
import webbrowser
from requests.exceptions import *
from .headers import headers_water
from rich import console,syntax
from .hopter import Error_pta,Error_ptb,Tip_pta
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

CoCo = console.Console()
headers = headers_water()

def hoget(url):
  global headers
  res = 0
  start_time = time.time()
  try:
    with console.Console().status("\033[96mLoading url …"):
      res = visit.get(url,headers=headers,stream=True,verify=False)
    if res.status_code == 200:
      end_time = time.time()
      total_time = end_time - start_time
      print('\033[32mUrl-Url:\033[0m\033[94m\n'+res.url) 
      print('\033[32mUrl-Time:\033[0m\033[94m\n'+str(total_time)+'S')
      with console.Console().status("\033[96mLoading information …"):
        print('\033[32mUrl-Szie:\033[0m\033[94m\n'+str(len(res.text))+'B')
      print('\033[32mUrl-Cookies:\033[0m\033[94m')
      for name, value in visit.utils.dict_from_cookiejar(res.cookies).items():
        print('├ %s:%s ' % (name, value))
      if not visit.utils.dict_from_cookiejar(res.cookies):
        print(None)
      print('\033[32mUrl-Headers:\033[0m\033[94m')
      for name, value in res.headers.items():
        print('├ %s:%s ' % (name, value))
      print('\033[32mUrl-Requests-Headers:\033[0m\033[94m')
      for name, value in res.request.headers.items():
        print('├ %s:%s ' % (name, value))
      print('\033[92mUrl-Code-Coding:\033[0m\033[94m\n'+str(res.encoding))
      if res.encoding != None:
        print('\033[92mUrl-Code-Type:\033[0m\033[94m\nGeneral network\033[0m')
        res.encoding = chardet.detect(res.content)['encoding']
        with console.Console().status("\033[96mLoading text …\033[0m"):
          print('\033[92mUrl-Code-Content:\033[0m')
          CoCo.print(syntax.Syntax(res.text,'html',theme="ansi_dark", line_numbers=True))
      else:
        print('\033[92mUrl-Code-Type:\033[0m\033[94m\nOther network')
        with console.Console().status("\033[96mLoading text …\033[0m"):
          print('\033[92mUrl-Code-Content:\033[0m')
          CoCo.print(syntax.Syntax(str(res.content),'html',theme="ansi_dark", line_numbers=True))
    else:
      Error_pta(str(res.status_code)+'Error','Command',str(res.status_code)+' Error in request','hoget …')
  except HTTPError as e:
    Error_pta('HTTPError','Command',str(e),'hoget …')
  except SSLError as e:
    Error_pta('SSLError','Command',str(e),'hoget …')
  except ConnectionError as e:
    Error_pta('ConnectionError','Command',str(e),'hoget …')
  except RequestException as e:
    Error_pta('RequestException','Command',str(e),'hoget …')
 
def browser_get(url):
  webbrowser.open(url) 
  Tip_pta('The program has opened the URL in the browser')
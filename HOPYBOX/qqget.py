import json
import requests as visit
from .headers import *
from .hopter import Error_pta,Tip_pta
headers = headers_water()
def qqhead(qq):
  global header
  qqres = visit.get('http://q2.qlogo.cn/headimg_dl?dst_uin={}&spec=100'.format(qq),headers=headers)
  with open(qq+'.jpg', 'wb') as file:
    file.write(qqres.content)
    Tip_pta('Get head picture win,already save in the file')
def qqname(qq):
  if qq:
    global header
    qqres = visit.get('http://api.usuuu.com/qq/'+str(qq),headers=headers).content
    qqres = json.loads(qqres)
    try:
      qqname = qqres['data']['name']
      if not qqname == '':
        print('\033[92m{}'.format(qqname))
      else:
        Error_pta('NotFoundQQErrorError','Command','Unrecognized instruction','qqname'+qq)
    except:
      Error_pta('NotFoundQQErrorError','Command','Unrecognized instruction','qqname '+qq)
  else:
      Error_pta('NotFoundOrderError','Command','Please enter a command','qqname '+qq)
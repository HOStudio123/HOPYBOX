import requests as visit
from bs4 import BeautifulSoup as bs
from .translate import translate as tran
from .hopter import Error_pta
from .headers import headers_water
from .translate import translate
headers = headers_water()

def way_four(ip):
  res = visit.get('https://q.ip5.me/?s='+ip,headers=headers)
  soup = bs(res.text,'lxml')
  items = soup.find_all('div',style='color:#FF0000; word-break:break-all;')
  way_js = str(items).split('>')
  ipfway = str(str(way_js[1].split()).split('<')[0]).split('[\'')
  if '\', \'' in ipfway[1]:
    ipffway = str(ipfway[1]).split('\', \'')
    print('\033[92m{}'.format(translate(ipffway[0]+ipffway[1])))
  elif ipfway[1] == 'IP地址不合法，仅支持IPv4地址，且每次只能查询一个，请重新输入。' or ipfway[1] == '域名错误，无法解析，请输入准确的域名或IP地址。':
    Error_pta('NotFoundIPError','Command','An IP address query error occurred','ipget '+ip)
  elif ipfway[1] == '局域网对方和您在同一内部网':
    Error_pta('IPAddressError','Command','LAN\'s other parties and you are in the same internal network','ipget '+ip)
  else:
    print('\033[92m{}'.format(translate(ipfway[1])))
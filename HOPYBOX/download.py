import os
import ssl
import wget
import time
import requests as visit
from .headers import headers_water
from .hopter import Error_pta,Tip_pta

headers = headers_water()
ssl.SSLContext(ssl.PROTOCOL_TLSv1)

def download(url):
  print('\033[92m',end='\r')
  try:
    wget.download(url,'./')
    print('')
    Tip_pta('Successfully downloaded this file')
  except Exception as e:
    Error_pta('DownloadError','Command',str(e),'download …')    
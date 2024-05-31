import os
import ssl
import wget
from .headers import headers_water
from .hopter import Error_pta,Tip_pta

headers = headers_water()
ssl.SSLContext(ssl.PROTOCOL_TLSv1)

def download(url):
  print('\033[92m',end='\r')
  try:
    wget.download(url,'./')
    print('')
    download_path = os.getcwd()
    Tip_pta('Download successful! The file is stored in '+download_path)
  except Exception as e:
    Error_pta('DownloadError','Command',str(e),'download'+url)    
import os
import requests as visit
from bs4 import BeautifulSoup as bs
from .version import version_number as version
def check_version():
  global visit
  global version
  res = visit.get('https://hostudio123.github.io/HOPYBOX/version',timeout=None)
  with console.status("\033[35mDetecting in version …"):
    pass
  if version >= int(res.text):
    print("\033[96mResult:Your HOPYBOX is the latest version")
  else:
    print('\033[96mResult:New version found on the official website of HOPYBOX')
    os.system('python3 -m pip install -U HOPYBOX')
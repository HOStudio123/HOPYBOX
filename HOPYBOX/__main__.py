print('Loading Library …',end='\r')
from  getpass import getuser
from .version import version
from .helps import all_help,module_help
from .download import download
from .hopt import Error_pta
from .system import systems,runpy,python,install,uninstall
from .qqget import qqname,qqhead
from .urlget import hoget,browse_get
from .sdemail import sd_email
from .checkversion import check
from .caculate import kmath
print('\033[36mWELCOME TO HOPYBOX\033[0m\033[32m [{}]\033[0m\n{}'.format(getuser().upper(),version))
pattern = 'Command'
while True:
  answer = input('\033[0m\033[33mHOPYBOX/{}:\033[0m'.format(pattern))
  if answer == 'exit':
    exit()
  elif answer == 'take command':
    pattern = 'Command'
  elif answer == 'take system':
    pattern = 'System'
  elif answer == 'take python':
    pattern = 'Python'
  #Command
  elif pattern == 'Command':
    if answer == 'help':
      all_help()
    elif answer[:5] == 'help ':
      module_help(answer[5:])
    elif answer == 'version':
      print('\033[0m\033[32m{}'.format(version))
    elif answer[:4] == 'run ':
      runpy(answer[4:])
    elif answer[:9] == 'download ':
      download(answer[9:])
    elif answer[:6] == 'hoget ':
      hoget(answer[6:])
    elif answer[:7] == 'bowget ':
      browse_get(answer[7:])
    elif answer[:5] == 'open ':
      read_file(answer[5:])
    elif answer[:10] == 'translate ':
      translate(answer[10:])
    elif answer[:3] == 'id ':
      print('\033[32m'+str(id(answer[3:])))
    elif answer[:7] == 'qqname ':
      qqname(answer[7:])
    elif answer[:7] == 'qqhead':
      qqhead(answer[7:])
    elif answer[:6] == 'email ':
      sd_email(answer[6:])
    elif answer[:4] == 'cat ':
      kmath(answer[4:])
    elif answer == 'check':
      check()  
    elif answer[:8] == 'install ':
      install(answer[8:])
    elif answer[:10] == 'uninstall ':
      uninstall(answer[10:])
    elif not answer:
      Error_pta('NotFindOrderError',pattern,'Please enter a command',answer)
    else:
      Error_pta('OrderError',pattern,'Unrecognized instruction',answer)
  #System
  elif pattern == 'System':
    if answer:
      systems(answer)
    else:
      Error_pta('NotFindOrderError',pattern,'Please enter a command',answer)
  #Python
  elif pattern == 'Python':
    if answer == 'interpreter':
      python()
    else:
      Error_pta('OrderError',pattern,'Unrecognized instruction',answer)
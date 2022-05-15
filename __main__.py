#-*- coding:utf-8 -*-
from rich.console import Console
console = Console()
#Loading library
with console.status("\033[35mLoading library …"):
  import readline
  import rlcompleter
  from  getpass import getuser
  from .version import version
  from .download import download
  from .hopter import (
      Error_pta,
      Tip_pta
)
  from .system import (
      systems,
      runpy,
      python,
      install,
      uninstall,
      debug,
      all_help,
      module_help,
      license,
      pip_list
)
  from .qqget import (
      qqname,
      qqhead
)
  from .urlget import (
      hoget,
      browse_get
)
  from .sdemail import sd_email
  from .check import check_version
  from .caculate import (
      caculate,
      root_caculate,
      triangle_caculate
)
  from .translate import translate
  from .findipway import way_four
  from .filetoolbox import read_file
  from .weather import city
#Main program header
print('\033[96mWELCOME TO HOPYBOX\033[0m\033[92m [USER:{}]\033[0m\n{}'.format(getuser().upper(),version))
#Main program variables
pattern = 'Command'
#The main block of code
while True:
  answer = input('\033[0m\033[93mHOPYBOX/{}:\033[0m'.format(pattern))
  if answer == 'exit':
    exit()
  elif answer == 'take command':
    pattern = 'Command'
    Tip_pta('Program mode switched successfully')
  elif answer == 'take system':
    pattern = 'System'
    Tip_pta('Program mode switched successfully')
  elif answer == 'take python':
    pattern = 'Python'
    Tip_pta('Program mode switched successfully')
  #Command
  elif pattern == 'Command':
    if answer == 'help':
      all_help()
    elif answer[:5] == 'help ':
      module_help(answer[5:])
    elif answer == 'license':
      license()
    elif answer == 'version':
      print(version)
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
    elif answer == 'check version':
      check_version()
    elif answer[:10] == 'caculate √':
      root_caculate(answer[10:])
    elif answer[:10] == 'caculate |':
      abs_caculate(answer[10:])
    elif answer[:9] == 'triangle ':
      triangle_caculate(answer[9:])
    elif answer[:9] == 'caculate ':
      caculate(answer[9:])
    elif answer[:8] == 'install ':
      install(answer[8:])
    elif answer[:10] == 'uninstall ':
      uninstall(answer[10:])
    elif answer[:8] == 'fwayget ':
      way_four(answer[8:])
    elif answer[:8] == 'weather ':
      city(answer[8:])
    elif answer == 'pack list':
      pip_list()
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
    elif answer[:6] == 'debug ':
      debug(answer[6:])
    else:
      Error_pta('OrderError',pattern,'Unrecognized instruction',answer)
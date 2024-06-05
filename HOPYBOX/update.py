from rich.console import Console
from .basedtool import clear
from .basedtool import terminal
from requests import get
from .prompt import tip_tick
from .prompt import error_cross
from .prompt import ask_proceed

console = Console()
update_version_number = 169
update_log_content = {}

def update_log_add(version,date,text):
  update_log_content[f'{version}'] = {'date':f'{date}','update':f'{text}'}

update_log_add('0.0.1','May 2, 2022','* This is the first version of HOPYBOX posted on PyPI, but not the first version of HOPYBOX, The first version was born around Jan 28, 2022')
update_log_add('0.9.6','May 2, 2022','* Updated program error\n* Added function to open files\n* Fixed some known issues')
update_log_add('1.2.0','May 8 2022','* Added calculator function\n* Fixed some known issues',)
update_log_add('1.3.4','May 15 2022','* Fixed some known issues')
update_log_add('1.3.5','May 21, 2022','* Fixed some known issues')
update_log_add('1.3.6','May 21, 2022','* Fixed some known issues')
update_log_add('1.3.7','May 22, 2022','* Fixed some known issues')
update_log_add('1.3.8','May 22, 2022','* Fixed some known issues')
update_log_add('1.3.9','May 22, 2022','* Fixed some known issues')
update_log_add('1.4.1','May 24, 2022','* Fixed some known issues')
update_log_add('1.4.2','May 24, 2022','* Fixed some known issues')
update_log_add('1.4.3','May 24, 2022','* Fixed some known issues')
update_log_add('1.4.4','May 24, 2022','* Fixed some known issues')
update_log_add('1.4.5','May 25, 2022','* Fixed some known issues')
update_log_add('1.4.6','May 26, 2022','* Fixed some known issues')
update_log_add('1.4.7','May 27, 2022','* Fixed some known issues')
update_log_add('1.4.8','May 28, 2022','* Fixed some known issues')
update_log_add('1.4.9','May 28, 2022','* Fixed some known issues')
update_log_add('1.5.0','May 28, 2022','* Fixed some known issues')
update_log_add('1.5.1','May 28, 2022','* Fixed some known issues')
update_log_add('1.5.2','May 28, 2022','* Fixed some known issues')
update_log_add('1.5.3','May 28, 2022','* Fixed some known issues')
update_log_add('1.5.5','May 28, 2022','* Fixed some known issues')
update_log_add('1.5.6','May 28, 2022','* Fixed some known issues')
update_log_add('1.5.8','May 30, 2022','* Fixed some known issues')
update_log_add('1.6.0','May 30, 2022','* Fixed some known issues')
update_log_add('1.6.1','May 30, 2022','* Fixed some known issues')
update_log_add('1.6.3','Jun 14, 2022','* Fixed some known issues')
update_log_add('1.6.4','Jul 9, 2022','* Fixed some known issues')
update_log_add('1.6.5','Dec 23, 2022','* Fixed some known issues')
update_log_add('1.6.6','Feb 3, 2023','* Fixed some known issues')
update_log_add('1.6.7','Feb 3, 2023','* Fixed some known issues')
update_log_add('1.7.0','Oct 10 2023','* Removed some commands\n* Add some new commands\n* Code structure optimization\n* Import method update\n* Fixed some known issues')
update_log_add('1.7.1','Jun 1 2024','* Removed some commands\n* Add some new commands\n* Code structure optimization\n* Import method update\n* Fixed some known issues')
update_log_add('1.7.2','Jun 1 2024','* Removed some commands\n* Add some new commands\n* Code structure optimization\n* Import method update\n* Fixed some known issues')


def update_log_get(version):
  try:
    print(f'\033[96mHOPYBOX {version} Update Data\033[0m\033[92m ('+update_log_content[version]['date']+')\033[0m\n\033[95m'+update_log_content[version]['update'])
  except KeyError:
   error_cross('NotFoundVersionError','Command','No update log found for this version',f'update {version}')
   
def update_program():
  try:
    with console.status("\033[96mChecking in version …"):
      res = get('https://hopybox.github.io/version')
    if update_version_number >= int(res.text):
      tip_tick('It is already the latest version')
    else:
      while True:
        result = ask_proceed('There is a latest stable version discovered from PyPI')
        if result == True:
          terminal('python3 -m pip install -U HOPYBOX')
          tip_tick('Please restart the program manually')
          exit()
        elif result == None:
          continue
        else:
          break
  except Exception:
    error_cross('CheckError','Command','Failed to get update','check version')
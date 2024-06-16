'''
Copyright (c) 2022-2024 HOStudio123(ChenJinlin).
All Rights Reserved.
'''

#!/usr/bin/env python3

# -*- coding:utf-8 -*-

from rich.console import Console
with Console().status("\033[96mLoading resources …\033[0m"):
  import os,re
  # prompt_toolkit
  from prompt_toolkit import PromptSession
  from prompt_toolkit.styles import Style
  from prompt_toolkit.completion import WordCompleter
  # datetime
  from datetime import datetime
  # getpass
  from getpass import getuser
  # platform
  from platform import system
  from platform import python_version
  # device
  from .device import device
  # prompt
  from .prompt import error_cross
  from .prompt import tip_tick
  # connect
  from .connect import hoget
  from .connect import browser
  from .connect import download
  # mail
  from .mail import email
  # translate
  from .translate import langdet
  from .translate import translate
  # command
  from .command import command_help
  from .command import command_data
  from .command import command_data_add
  # update
  from .update import update_log_get
  from .update import update_log_content
  from .update import update_program
  # calculate
  from .calculate import calculate
  # filetool
  from .filetool import filetool
  from .filetool import tree
  from .filetool import scanner
  # timetool
  from .timetool import timetool
  # license
  from .LICENSE import license
  # TOTP
  from .totp import totp
  # some information of hopybox
  __author__ = 'HOStudio123(ChenJinlin)'
  __email__ = 'hostudio.hopybox@foxmail.com'
  __license__ = 'GPL-3.0 license'
  __copyright__ = 'Copyright (c) 2022-2024 HOStudio123(ChenJinlin).\nAll Rights Reserved.'    
  # mode
  _mode_type = ['Program','Device','File','Calculate']
  _mode = _mode_type[0]
  # windows
  _windows = 0
  # version
  _version_code = '1.7.6'
  _version_type = 'default'
  _version_all = f'\033[95m* HOPYBOX Version {_version_code}\n* Python Version {python_version()}'
  # update time
  _update_time = '14:34:00'
  # command
  command_data_add()
  # store system
  _store = ''
  # hopybox artword
  hopybox_artword = '''
 _   _  _____  ____  __     __ ____  _____  __  __                     
| | | ||  _  ||  _ \ \ \   / /|  _ \|  _  | \ \/ /                  
| |_| || | | || |_| | \ \_/ / | |_| | | | |  \  /                      
|  _  || | | ||  __/   \   /  |  _ <| | | |  /  \                      
| | | || |_| || |       | |   | |_| | |_| | / /\ \                     
|_| |_||_____||_|       |_|   |____/|_____|/_/  \_\                    
 
  '''
  # start text
  print(f"\033[96mWELCOME TO HOPYBOX\n\033[0m\033[92m[USER:{getuser().upper()}] [RUN:{datetime.now().strftime('%H:%M:%S')}]\033[0m\nHOPYBOX {_version_code} ({_version_type}, {update_log_content[_version_code]['date']}, {_update_time})\n[Python {python_version()}] on {system()}\nType \"help\" , \"copyright\" , \"version\" ,\"feedback\" or \"license\" for more information")
  
def terminal(command):
  os.system(command)

def clear():
  print("\033c",end="")
  terminal('cls' if os.name == 'nt' else 'clear')
  
# switch mode
def _switch(mode):
  global _mode, _command_list
  if mode.title() in _mode_type:
    _mode = mode.title()
    _command_list.clear()
    [_command_list.append(i) for i in command_data[_mode]]
    [_command_list.append(j) for j in command_data['Global']]
    tip_tick('Program mode switched successfully')
  else:
    error_cross('SwitchError',_mode,'The mode was not found',_store.split(' ',1)[1])

# exception
class NotFoundCommandError(Exception):
  def __init__(self):
    super().__init__('This command was not found in this mode')

def _history_add():
  global _store
  if _store not in _history:
    if _history:
      del _history[-1]
    _history.append(_store)

# command process
def _process(command,blank=2):
 return command.split(' ',blank)
 
# interpreter
def run(command):
  global _command
  _command = _process(command)[0]
  try:
    if _command in command_data['Global']:
      if len(_process(command)) != 1:
        command_data['Global'][_command]['run'] = _process(command)[1]
      exec(command_data['Global'][_command]['code'])  
      _history_add()
    elif _command in command_data[_mode]:
      if len(_process(command)) == 1:
        exec(command_data[_mode][_command]['code'])
        _history_add()
      else:
        if _process(command)[1][0] == '-':
          if len(_process(command)) == 3:
            command_data[_mode][_command]['run'] = _process(command)[2]
          exec(command_data[_mode][_command]['code'][_process(command)[1]])
          _history_add()
        else:
          if len(_process(command)) < 3:
            command_data[_mode][_command]['run'] = _process(command)[1]
          else:
            command_data[_mode][_command]['run'] = _process(command,blank=1)[1]
          exec(command_data[_mode][_command]['code'])
          _history_add()
    else:
      raise NotFoundCommandError
  except Exception as e:
    error_cross(e.__class__.__name__,_mode,e,_store)
    try:
      del command_data[_mode][_command]['run']
    except:
      try:
        del command_data['Global'][_command]['run']
      except:
        pass
  
# start
def start():
  global _command, _store, _windows, _history, _command_list
  _history = list()
  style = Style.from_dict({'prompt':'yellow'})
  _command_list=list()
  [_command_list.append(i) for i in command_data[_mode]]
  [_command_list.append(j) for j in command_data['Global']]
  completer = WordCompleter(_command_list)
  session = PromptSession(style=style)
  while True:
    _windows+=1
    try:
      _command = session.prompt(f'[{_windows}]HOPYBOX/{_mode}:',completer=completer,style=style)
    except EOFError:
      exit()
    except KeyboardInterrupt:
      continue
    _store = _command
    run(_command)
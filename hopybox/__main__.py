'''
Copyright (c) 2022-2024 HOStudio123(ChenJinlin).
All Rights Reserved.
'''

#!/usr/bin/env python3

# -*- coding:utf-8 -*-

import os,re

# color
if os.name == 'nt':
  os.system('')

# make dir
if not os.path.isdir(os.path.join(os.path.expanduser('~'),'.hopybox')):
  os.mkdir(os.path.join(os.path.expanduser('~'),'.hopybox'))
  os.mkdir(os.path.join(os.path.expanduser('~'),'.hopybox','.File_Recycle'))

from rich.console import Console
with Console().status("\033[96mLoading resources …\033[0m"):
  # prompt_toolkit
  from prompt_toolkit import PromptSession
  from prompt_toolkit.styles import Style
  from prompt_toolkit.completion import NestedCompleter
  from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
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
  from .filetool import editingtool
  from .filetool import tree
  from .filetool import bin_system
  from .filetool import scanner
  # timetool
  from .timetool import timetool
  # license
  from .LICENSE import license
  # cipher
  from .cipher import cipher
  from .cipher import two_factor
  # some information of hopybox
  __author__ = 'HOStudio123'
  __email__ = 'hostudio.hopybox@foxmail.com'
  __license__ = 'GPL-3.0 license'
  __copyright__ = 'Copyright (c) 2022-2024 HOStudio123.\nAll Rights Reserved.'    
  # mode
  _mode_type = ['Program','Device','File','Calculate']
  _mode = _mode_type[0]
  # windows
  _windows = 0
  # version
  _version_code = '1.9.4'
  _version_type = 'default'
  _version_all = f'\033[95m* HOPYBOX Version {_version_code}\n* Python Version {python_version()}'
  # update time
  _update_time = '19:30:00'
  # command
  command_data_add()
  # store system
  _store = ''
  # hopybox artword
  hopybox_artword = '''\033[96m
 _   _  _____  ____  __     __ ____  _____  __  __                     
| | | ||  _  ||  _ \ \ \   / /|  _ \|  _  | \ \/ /                  
| |_| || | | || |_| | \ \_/ / | |_| | | | |  \  /                      
|  _  || | | ||  __/   \   /  |  _ <| | | |  /  \                      
| | | || |_| || |       | |   | |_| | |_| | / /\ \                     
|_| |_||_____||_|       |_|   |____/|_____|/_/  \_\    

This is an open-source and practical command box.                
  '''
  # hopybox update log
  update_log_dict = dict()
  update_log_dict['all'] = None
  for i in update_log_content:
    update_log_dict[i] = None

# command prompt list
def help_list_update():
  global command_prompt_list
  command_prompt_list = set()
  [command_prompt_list.add(j) for j in command_data['Global']]
  [command_prompt_list.add(j) for j in command_data[_mode]]
  
def terminal(command):
  os.system(command)

def clear():
  print("\033c",end="")
  terminal('cls' if os.name == 'nt' else 'clear')
  
# switch mode
def _switch(mode):
  global _mode, completer
  if mode.title() in _mode_type:
    _mode = mode.title()
    completer = NestedCompleter.from_nested_dict(_format_command())
    tip_tick('Program mode switched successfully')
  else:
    error_cross('SwitchError',_mode,'The mode was not found',_store.split(' ',1)[1])

# exception
class NotFoundCommandError(Exception):
  def __init__(self):
    super().__init__('This command was not found in this mode')
    
# command process
def _process(command):
  split_list = command.split()
  if len(split_list) <= 2:
    return command.split()
  command = split_list[0]
  parameter = split_list[1]
  if parameter[0] == '-':
    content = split_list[2:]
    if len(content) == 1:
      content=content[0]
    return [command,parameter,content]
  content = split_list[1:]
  return [command,content]

# interpreter
def analysis(mode,command):
  global _command
  if len(_process(command)) == 1:
    exec(command_data[mode][_command]['code'])
  else:
    if _process(command)[1][0] == '-':
      if len(_process(command)) == 3:
        command_data[mode][_command]['run'] = _process(command)[2]
      exec(command_data[mode][_command]['code'][_process(command)[1]])
    else:
      command_data[mode][_command]['run'] = _process(command)[1]
      exec(command_data[mode][_command]['code'])
  
def run(command):
  global _command
  _command = _process(command)[0] if command else ''
  try:
    if _command in command_data['Global']:
      analysis('Global',command)
      try:
        del command_data['Global'][_command]['run']
      except:
        pass
    elif _command in command_data[_mode]:
      analysis(_mode,command)
      try:
        del command_data[_mode][_command]['run']
      except:
        pass
    else:
      raise NotFoundCommandError
  except Exception as e:
    error_cross(e.__class__.__name__,_mode,e,_store)

# command formatting
def _format_command():
  global _mode, command_prompt_list
  command_dict = dict()
  for i in command_data[_mode]:
    if type(command_data[_mode][i]['code']) == str:
      command_dict[i] = update_log_dict if i == 'uplog' else None
    else:
      par_set = set()
      [par_set.add(j) for j in command_data[_mode][i]['code']]
      command_dict[i] = par_set
      del par_set
  for i in command_data['Global']:
    if type(command_data['Global'][i]['code']) == str:
      if i == 'switch':
        command_dict[i] = {'Program','Device','File','Calculate'}
      elif i == 'help':
        help_list_update()
        command_dict[i] = command_prompt_list
      else:
        command_dict[i] = None
    else:
      par_set = set()
      [par_set.add(j) for j in command_data['Global'][i]['code']]
      command_dict[i] = par_set
  return command_dict

# start
def start():
  global _command, _store, _windows, completer
  mouse_support = False
  times = 0
  # start text
  print(f"\033[96mWELCOME TO HOPYBOX\n\033[0m\033[92m[USER:{getuser()}] [RUN:{timetool.hms}]\033[0m\nHOPYBOX {_version_code} ({_version_type}, {update_log_content[_version_code]['date']}, {_update_time})\n[Python {python_version()}] on {system()}\nType \"help\" , \"copyright\" , \"version\" ,\"feedback\" or \"license\" for more information")
  style = Style.from_dict({'prompt':'yellow'})
  completer = NestedCompleter.from_nested_dict(_format_command())
  session = PromptSession(style=style)
  while True:
    _windows+=1
    try:
      _command = session.prompt(f'[{_windows}]HOPYBOX/{_mode}:',completer=completer,style=style,mouse_support=mouse_support,auto_suggest=AutoSuggestFromHistory())
    except EOFError:
      exit()
    except KeyboardInterrupt:
      times+=1
      if times%2!=0:
        mouse_support = True
        tip_tick('Successfully turned on mouse mode')
      else:
        mouse_support = False
        tip_tick('Successfully turned off mouse mode')
      continue
    _store = _command
    run(_command)
    
if __name__ == '__main__':
  start()
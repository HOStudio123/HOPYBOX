'''
Copyright (c) 2022-2024 HOStudio123(ChenJinlin).
All Rights Reserved.
'''

#!/usr/bin/env python3

# -*- coding:utf-8 -*-

from rich.console import Console
with Console().status("\033[96mLoading resources …\033[0m"):
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
  # mail
  from .mail import email
  # translate
  from .translate import translate
  # command
  from .command import par
  from .command import command_help
  from .command import command_data
  from .command import command_data_add
  # update
  from .update import update_log_get
  from .update import update_log_content
  from .update import update_program
  # caculate
  from .caculate import caculate
  # filetool
  from .filetool import filetool
  # timetool
  from .timetool import timetool
  # based operate
  from .basedtool import terminal
  from .basedtool import clear
  from .basedtool import char
  # license
  from .LICENSE import license
  # some information of hopybox
  __author__ = 'HOStudio123(ChenJinlin)'
  __email__ = 'hostudio.hopybox@foxmail.com'
  __license__ = 'GPL-3.0 license'
  __copyright__ = 'Copyright (c) 2022-2024 HOStudio123(ChenJinlin).\nAll Rights Reserved.'    
  # mode
  _mode_type = ['Program','Device','File','Caculate']
  _mode = _mode_type[0]
  # windows
  _windows = 0
  # version
  _version_code = '1.7.2'
  _version_type = 'default'
  _version_all = f'\033[95m* HOPYBOX Version {_version_code}\n* Python Version {python_version()}'
  # update time
  _update_time = '14:37:50'
  # command
  command_data_add()
  # start text
  print(f"\033[96mWELCOME TO HOPYBOX\n\033[0m\033[92m[USER:{getuser().upper()}] [FPS:{device.Fps().fps()}] [RUN:{datetime.now().strftime('%H:%M:%S')}]\033[0m\nHOPYBOX {_version_code} ({_version_type}, {update_log_content[_version_code]['date']}, {_update_time})\n[Python {python_version()}] on {system()}\nType \"help\" , \"copyright\" , \"version\" ,\"feedback\" or \"license\" for more information")

# switch mode
def _switch(mode):
  global _mode
  if mode.title() in _mode_type:
    _mode = mode.title()
    tip_tick('Program mode switched successfully')
  else:
    error_cross('SwitchError',_mode,'The mode was not found',_store)

# exception
class NotFoundCommandError(Exception):
  def __init__(self):
    super().__init__('This command was not found')

# command process
def _process(command):
 return command.split(' ',1)
 
# interpreter
def run(command):
  global _command
  _command = _process(command)[0]
  try:
    if _command in command_data[_mode]:
      if len(_process(command)) == 1:
        exec(command_data[_mode][_command]['code'])
      else:
        if _process(command)[1][0] == '-':
          exec(command_data[_mode][_command]['code'][_process(command)[1]])
        else:
          command_data[_mode][_command]['run'] = _process(command)[1]
          exec(command_data[_mode][_command]['code'])
    else:
      raise NotFoundCommandError
  except Exception as e:
    error_cross(e.__class__.__name__,_mode,e,_store)
    try:
      del command_data[_mode][_command]['run']
    except:
      pass
  
# start
def start():
  global _command, _store, _windows
  while True:
    _windows+=1
    _command = input(f'\033[0m\033[93;1m[{_windows}]\033[0m\033[93mHOPYBOX/{_mode}:\033[0m')
    _store = _command
    run(_command)
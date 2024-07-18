#!/usr/bin/env python3

# -*- coding:utf-8 -*-

'''
Copyright (c) 2022-2024 HOStudio123.
All Rights Reserved.
'''

import os, re
import subprocess

# make data dir
os.makedirs(os.path.join(os.path.expanduser('~'),'.config','hopybox','.File_Recycle'),exist_ok=True)

from rich.console import Console

console = Console()

with console.status('[bright_cyan]Loading resources …[/bright_cyan]'):
    # prompt_toolkit library
    from prompt_toolkit.styles import Style
    from prompt_toolkit import PromptSession
    from prompt_toolkit.completion import NestedCompleter
    from prompt_toolkit.formatted_text import FormattedText
    from prompt_toolkit import print_formatted_text as print
    from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

    # getpass library
    from getpass import getuser

    # platform library
    from platform import system
    from platform import python_version

    # device library
    from .device import device

    # prompt library
    from .prompt import error_cross
    from .prompt import tip_tick

    # connect library
    from .connect import hoget
    from .connect import browser
    from .connect import download

    # mail library
    from .mail import email

    # translate library
    from .translate import langdet
    from .translate import translate

    # command library
    from .command import command_help
    from .command import command_data
    from .command import command_data_add

    # update library
    from .update import update_log_format
    from .update import update_program

    # calculate library
    from .calculate import calculate

    # filetool library
    from .filetool import filetool
    from .filetool import editingtool
    from .filetool import tree
    from .filetool import bin_system
    from .filetool import scanner

    # timetool library
    from .timetool import timetool

    # license
    from .LICENSE import license

    # cipher library
    from .cipher import cipher
    from .cipher import two_factor

    # some information of hopybox
    __author__ = 'HOStudio123'
    __email__ = 'hostudio.hopybox@foxmail.com'
    __license__ = 'GPL-3.0 license'
    __copyright__ = 'Copyright (c) 2022-2024 HOStudio123.\nAll Rights Reserved.'
    
    # mode
    _mode_type = ['Program', 'Device', 'File', 'Calculate']
    _mode = _mode_type[0]
    
    # windows
    _windows = 0
    
    # version
    _version_code = '1.9.8'
    _version_number = int(''.join(_version_code.split('.')))
    _version_type = 'default'
    _version_info = f'\033[95m* HOPYBOX Version {_version_code}\n* Python Version {python_version()}'
    _version_update_content = '* Fixed some known issues\n* Add some new commands'
    _version_update_time = 'Jul 17 2024 10:05:00'
    
    # command
    command_data_add()
    
    # store system
    _store = ''
    
    # hopybox artword
    hopybox_artword = r'''
 _   _  _____  ____ __     __ ____  _____  __  __                     
| | | ||  _  ||  _ \\ \   / /|  _ \|  _  | \ \/ /                  
| |_| || | | || |_| |\ \_/ / | |_| | | | |  \  /                      
|  _  || | | ||  __/  \   /  |  _ <| | | |  /  \                      
| | | || |_| || |      | |   | |_| | |_| | / /\ \                     
|_| |_||_____||_|      |_|   |____/|_____|/_/  \_\    

This is an open-source and practical command box.                
  '''

# command prompt list
def help_list_update():
    global command_prompt_list
    command_prompt_list = set()
    [command_prompt_list.add(j) for j in command_data['Global']]
    [command_prompt_list.add(j) for j in command_data[_mode]]


def terminal(command):
    os.system(command)


def clear():
    print('\033c', end='')
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

# switch mode
def _switch(mode):
    global _mode, completer
    if mode.title() in _mode_type:
        _mode = mode.title()
        completer = NestedCompleter.from_nested_dict(_format_command())
        tip_tick('Program mode switched successfully')
    else:
        error_cross('SwitchError', _mode, 'The mode was not found', _store.split(' ', 1)[1])


# exception
class NotFoundCommandError(Exception):
    def __init__(self):
        super().__init__('This command was not found in this mode')


# command process
def _process(command:str) -> list:
    split_list = command.split()
    if len(split_list) <= 2:
        return command.split() # list
    command = split_list[0]
    parameter = split_list[1]
    if parameter[0] == '-':
        content = split_list[2:]
        if len(content) == 1:
            content = content[0]
        return [command, parameter, content] # list
    content = split_list[1:]
    return [command, content] # list


# interpreter
def analysis(mode, command):
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
            analysis('Global', command)
            try:
                del command_data['Global'][_command]['run']
            except:
                pass
        elif _command in command_data[_mode]:
            analysis(_mode, command)
            try:
                del command_data[_mode][_command]['run']
            except:
                pass
        else:
            raise NotFoundCommandError
    except Exception as e:
        error_cross(e.__class__.__name__, _mode, e, _store)


# command formatting
def _format_command():
    global _mode, command_prompt_list
    command_dict = dict()
    for i in command_data[_mode]:
        if type(command_data[_mode][i]['code']) == str:
            command_dict[i] = None
        else:
            par_set = set()
            [par_set.add(j) for j in command_data[_mode][i]['code']]
            command_dict[i] = par_set
            del par_set
    for i in command_data['Global']:
        if type(command_data['Global'][i]['code']) == str:
            if i == 'switch':
                command_dict[i] = {'Program', 'Device', 'File', 'Calculate'}
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
    text = FormattedText([
    ('class:title', 'WELCOME TO HOPYBOX'),
    ('', '\n'),
    ('class:head', f'[USER:{getuser()}] [RUN:{timetool.hms}]'),
    ('', '\n'),
    ('class:body', f"HOPYBOX {_version_code} ({_version_type}, {' '.join(_version_update_time.split()[:3])}, {_version_update_time.split()[3]})\n[Python {python_version()}] on {system()}\nType \"help\" , \"copyright\" , \"version\" ,\"feedback\" or \"license\" for more information")
    ])
    style = Style.from_dict({
    'title': '#00ffff',
    'head': '#00ff00',
    })
    print(text,style=style)
    style = Style.from_dict({'prompt': 'yellow'})
    completer = NestedCompleter.from_nested_dict(_format_command())
    session = PromptSession(style=style)
    while True:
        _windows += 1
        try:
            _command = session.prompt(f'[{_windows}]HOPYBOX/{_mode}:',completer=completer,style=style,mouse_support=mouse_support,auto_suggest=AutoSuggestFromHistory())
        except EOFError:
            exit()
        except KeyboardInterrupt:
            times += 1
            if times % 2 != 0:
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
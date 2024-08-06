# -*- coding:utf-8 -*-

'''
Copyright (c) 2022-2024 HOStudio123 (hostudio.hopybox@foxmail.com).
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
    from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

    # getpass library
    from getpass import getuser

    # platform library
    from platform import node
    from platform import system
    from platform import python_version

    # device library
    from .device import device

    # prompt library
    from .prompt import tip_tick
    from .prompt import error_cross
    from .prompt import error_cross_simple
    from .prompt import color_print

    # connect library
    from .connect import hoget
    from .connect import browser
    from .connect import download

    # mail library
    from .mail import email

    # translate library
    from .translate import translate

    # command library
    from .command import command_gather
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
    
    # ai library
    from .ai import coral

    # some information of hopybox
    __author__ = 'HOStudio123'
    __email__ = 'hostudio.hopybox@foxmail.com'
    __license__ = 'GPL-3.0 license'
    __copyright__ = 'Copyright (c) 2022-2024 HOStudio123 (hostudio.hopybox@foxmail.com)'
    
    # mode
    _mode_type = ['Program', 'Device', 'File', 'Calculate']
    _mode = _mode_type[0]
    
    # version
    _version_code = '2.0.0'
    _version_number = int(''.join(_version_code.split('.')))
    _version_type = 'default'
    _version_info = f'* HOPYBOX Version {_version_code}\n* Python Version {python_version()}'
    _version_update_content = '* Fixed some known issues\n* Add some new commands'
    _version_update_time = 'Aug 03 2024 12:03:00'
    
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
    [command_prompt_list.add(j) for j in command_data]

# plug-in
def color(color):
    color_print(color,color)

# plug-in
def terminal(command):
    os.system(command)
    
# plug-in
def clear():
    print('\033c', end='')
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

# switch mode
def _switch(mode):
    global _mode, completer
    if mode.title() in _mode_type:
        _mode = mode.title()
        completer = NestedCompleter.from_nested_dict(_format_command())
        tip_tick(f'Switched to {mode} mode successfully')
    else:
        error_cross('SwitchError', _mode, 'The mode was not found', _store.split(' ',1)[1])


# exception
class NotFoundCommandError(Exception):
    def __init__(self):
        super().__init__('This command was not found in this mode')

class MissingParameters(Exception):
    def __init__(self,command):
        super().__init__(f'Missing required parameters. Type "help {command}" for more information')


# command process
def _analysis(command:str) -> list:
    return command.split()


# interpreter
def _interpreter(mode, command):
   result = _analysis(command)
   length = len(result)
   command = result[0]
   if length == 1:
       if type(command_data[mode][command]['code']) != dict:
           try:
               exec(command_data[mode][command]['code'])
           except KeyError:
               raise MissingParameters(command)
       else:
           raise MissingParameters(command)
   else:
       if type(command_data[mode][command]['code']) == dict:
           for i in command_data[mode][command]['code']:
               for j in result:
                   if i == j:
                       pos_par = result.index(j)
                       if length >= 3:
                           if pos_par == 1:
                               command_data[mode][command]['run'] = result[2:]
                           else:
                               command_data[mode][command]['run'] = result[1:pos_par]
                           break
           exec(command_data[mode][command]['code'][result[pos_par]])
       else:
           command_data[mode][command]['run'] = result[1] if length < 3 else result[1:]
           exec(command_data[mode][command]['code'])


def run(command):
    global _command, rprompt
    if len(_analysis(command)) > 0:
        _command = _analysis(command)[0]
    else:
        _command = None
    try:
        if _command in command_data['Global']:
            _interpreter('Global', command)
            try:
                del command_data['Global'][_command]['run']
            except:
                pass
        elif _command in command_data[_mode]:
            _interpreter(_mode, command)
            try:
                del command_data[_mode][_command]['run']
            except:
                pass
        else:
            raise NotFoundCommandError
    except Exception as e:
        error_cross(e.__class__.__name__, e, _command)
    

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
    global _mode, _command, _store, completer, rprompt
    mouse_support = True if os.name == 'nt' else False
    # start text
    text = [
    ('class:title', 'WELCOME TO HOPYBOX'),
    ('', '\n'),
    ('class:head', f'[USER:{getuser()}] [RUN:{timetool.hms}]'),
    ('', '\n'),
    ('class:body', f'HOPYBOX {_version_code} ({_version_type}, {" ".join(_version_update_time.split()[:3])}, {_version_update_time.split()[3]})\n[Python {python_version()}] on {system()}\nType "help", "copyright", "version", "feedback" or "license" for more information')
    ]
    style = {
    'title': '#00FFFF',
    'head': '#00FF00',
    }
    color_print(text,style,single=False)
    message_style = Style.from_dict({
    'up':'#FFFF00',
    'username':'#00FFFF',
    'at':'#FF00FF',
    'host':'#00FF00',
    'mode':'#FFD700',
    'arrow':'#FFFF00',
    'left':'#009FF5',
    'path':'underline #009FF5',
    'right':'#009FF5'
    })
    completer = NestedCompleter.from_nested_dict(_format_command())
    session = PromptSession(style=style)
    while True:
        try:
            message = [
            ('class:up','╭─ '),
            ('class:mode',f'[{_mode}] '),
            ('class:username', getuser()),
            ('class:at', '@'),
            ('class:host', f'{node()} '),
            ('class:left','(📂 '),
            ('class:path', f'{os.getcwd()}'),
            ('class:right',')'),
            ('','\n'),
            ('class:arrow','╰─>  ')
            ]
            _command = session.prompt(message,completer=completer,style=message_style,mouse_support=mouse_support,auto_suggest=AutoSuggestFromHistory())
            if not _command.strip():
                continue
        except EOFError:
            exit()
        except KeyboardInterrupt:
            continue
        _store = _command
        run(_command)


# python -m hopybox
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(start())
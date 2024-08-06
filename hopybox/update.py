# -*- coding:utf-8 -*-

'''
Copyright (c) 2022-2024 HOStudio123 (hostudio.hopybox@foxmail.com).
'''

import os
import requests

from rich.console import Console

from .prompt import tip_tick
from .prompt import ask_proceed
from .prompt import color_print
from .prompt import error_cross_simple

console = Console()

def update_log_format(version,date,content):
    text = [
    ('class:version',f'HOPYBOX {version} Update Data'),
    ('',' '),
    ('class:date',f'({date})'),
    ('','\n'),
    ('class:content',content)
    ]
    style = {
    'version':'#00FFFF',
    'date':'#00FF00',
    'content':'#FF00FF'
    }
    color_print(text,style,single=False)
def update_program(version_number):
    try:
        with console.status('[bright_cyan]Checking in version …[/bright_cyan]'):
            res = requests.get('https://hopybox.github.io/version')
        if version_number >= int(res.text):
            tip_tick('It is already the latest version')
        else:
            while True:
                result = ask_proceed('There is a latest stable version discovered from PyPI')
                if result == True:
                    os.system('python -m pip install -U hopybox')
                    tip_tick('Please restart the program manually')
                    exit()
                elif result == None:
                    continue
                else:
                    break
    except Exception:
        error_cross_simple('Failed to get update')

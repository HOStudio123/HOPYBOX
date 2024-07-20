import os
import requests

from rich.console import Console

from .prompt import tip_tick
from .prompt import ask_proceed
from .prompt import error_cross_simple

console = Console()

def update_log_format(version,date,content):
    print(f"\033[96mHOPYBOX {version} Update Data\033[0m\033[92m ({date})\033[0m\n\033[95m{content}")

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
                    os.system('python3 -m pip install -U HOPYBOX')
                    tip_tick('Please restart the program manually')
                    exit()
                elif result == None:
                    continue
                else:
                    break
    except Exception:
        error_cross_simple('Failed to get update')

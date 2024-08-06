# -*- coding:utf-8 -*-

'''
Copyright (c) 2022-2024 HOStudio123 (hostudio.hopybox@foxmail.com).
'''

import os
import time
import webbrowser
import requests

from rich import syntax
from rich.console import Console
from rich.progress import Progress
from rich.progress import BarColumn
from rich.progress import DownloadColumn
from rich.progress import TransferSpeedColumn
from rich.progress import TimeRemainingColumn

from .headers import headers_water

from .prompt import tip_tick
from .prompt import error_cross_simple
from .prompt import color_print

# Disable Security Request Warning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3.exceptions import InsecurePlatformWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

console = Console()
headers = headers_water()


class Hoget:
    def __init__(self):
        self.start_time = 0
        self.total_time = 0

    def main(self, url):
        self.time(True)
        with Console().status('[bright_cyan]Loading URL …[/bright_cyan]'):
            res = self.content(url)
        if res.status_code == requests.codes.ok:
            self.total_time = self.time(False)
            color_print('Uniform Resource Locator','#00FF00')
            color_print(res.url,'#FF00FF')
            color_print('Request Duration','#00FF00')
            color_print(f'{self.total_time} s','#FF00FF')
            color_print('Headers Information','#00FF00')
            for name, value in res.headers.items():
                color_print(f'[{name}] ','#FF00FF',end='')
                color_print(value,'#FFFFFF')
            color_print('Requests Headers','#00FF00')
            for name, value in res.request.headers.items():
                color_print(f'[{name}] ','#FF00FF',end='')
                color_print(value,'#FFFFFF')
            color_print('Cookies','#00FF00')
            for name, value in requests.utils.dict_from_cookiejar(res.cookies).items():
                color_print(f'[{name}] ','#FF00FF',end='')
                color_print(value,'#FFFFFF')
            if not requests.utils.dict_from_cookiejar(res.cookies):
                color_print('Null','#FFFFFF')
            color_print('Encoding','#00FF00')
            color_print(res.encoding,'#FF00FF')
            cache = res.content
            color_print('Web Page Size','#00FF00')
            color_print(self._format_size(len(cache)),'#FF00FF')
            color_print('Web Page Source','#00FF00')
            if res.encoding:
                self.content_output(cache.decode(res.encoding))
            else:
                print(cache)
        else:
            error_cross_simple(f'{res.status_code} Error in request')

    def time(self, state):
        if state:
            self.start_time = time.time()
        else:
            return time.time() - self.start_time

    def content(self, url):
        return requests.get(url, headers=headers, stream=True, verify=False)

    def content_output(self, content):
        console.print(
            syntax.Syntax(content, 'html', theme='ansi_dark', line_numbers=True)
        )

    def _format_size(self, size):
        if size == None:
            return None
        num = 0
        while size > 1024:
            size /= 1024
            num += 1
        unit_set = ['B', 'KIB', 'MIB', 'GIB', 'TIB', 'PIB']
        return f'{size:.2f} '.rstrip('.0').zfill(1) + unit_set[num]


hoget = Hoget()


def browser(url):
    try:
        webbrowser.open_new(url)
        tip_tick('The program has opened the URL in the browser')
    except Exception as e:
        error_cross_simple(e)


def download(url):
    save_path = os.path.join(os.getcwd(), os.path.basename(url))
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_length = int(r.headers.get('content-length', 0))
        with Progress(
            BarColumn(bar_width=None),
            '[progress.percentage]{task.percentage:>3.0f}%',
            DownloadColumn(),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
        ) as progress:
            color_print(f'Downloading {os.path.basename(url)}', '#FF00FF')
            download_task = progress.add_task(None, total=total_length)
            with open(save_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        progress.update(download_task, advance=len(chunk))
    progress.remove_task(download_task)
    tip_tick(f'The file was saved to {save_path}')

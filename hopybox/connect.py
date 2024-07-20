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
from .prompt import error_cross

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
        with Console().status('\033[96mLoading URL …'):
            res = self.content(url)
        if res.status_code == requests.codes.ok:
            self.total_time = self.time(False)
            print(
                f'\033[32mUniform Resource Locator\033[0m\033[95m\n{res.url}\n\033[32mRequest Duration\033[0m\033[95m\n{self.total_time} s'
            )
            with Console().status('\033[96mLoading information …'):
                cache = res.content
                print(
                    f'\033[32mWeb Page Size\033[0m\033[95m\n{self._format_size(len(cache))}'
                )
                print('\033[32mHeaders\033[0m\033[95m')
                for name, value in res.headers.items():
                    print('* %s:%s ' % (name, value))
                print('\033[32mRequests Headers\033[0m\033[95m')
                for name, value in res.request.headers.items():
                    print('* %s:%s ' % (name, value))
                print('\033[32mCookies\033[0m\033[95m')
                for name, value in requests.utils.dict_from_cookiejar(
                    res.cookies
                ).items():
                    print('* %s:%s ' % (name, value))
                if not requests.utils.dict_from_cookiejar(res.cookies):
                    print('None')
                print(f'\033[32mEncoding\033[0m\033[95m\n{res.encoding}')
            print('\033[32mContent\033[0m')
            if res.encoding:
                self.content_output(cache.decode(res.encoding))
            else:
                print(cache)
        else:
            error_cross(
                f'{res.status_code} Error',
                'Command',
                f'{res.status_code} Error in request',
                f'hoget {url}',
            )

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
        error_cross('OpenBrowserError', 'Command', e, f'browget {url}')


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
            print(f'\033[95mDownloading {os.path.basename(url)}')
            download_task = progress.add_task(None, total=total_length)
            with open(save_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        progress.update(download_task, advance=len(chunk))
    progress.remove_task(download_task)
    tip_tick(f'The file was saved to {save_path}')

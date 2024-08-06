import os
import sys
import time
import uuid
import json
import locale
import socket
import psutil
import datetime
import requests
import platform

from .prompt import color_print

class Device:
    def name(self):
        return platform.node()

    def type(self):
        return platform.machine()

    def bit(self):
        return platform.architecture()[0]

    def info(self):
        color_print('Operating System','#FF00FF',end=' ')
        print(platform.system())
        color_print('OS Release','#FF00FF',end=' ')
        print(platform.release())
        color_print('OS Version','#FF00FF',end=' ')
        print(platform.version())
        color_print('Machine Type','#FF00FF',end=' ')
        print(platform.machine())
        color_print('Processor','#FF00FF',end=' ')
        print(Device().Processor().info())
        color_print('CPU Count','#FF00FF',end=' ')
        print(os.cpu_count())
        color_print('Node Name','#FF00FF',end=' ')
        print(platform.node())
        color_print('Language','#FF00FF',end=' ')
        print(locale.getlocale()[0])
        color_print('Encode','#FF00FF',end=' ')
        print(locale.getlocale()[1])
        color_print('Locate IP','#FF00FF',end=' ')
        print(Device().Web().IP().local())
        color_print('Public IP','#FF00FF',end=' ')
        print(Device().Web().IP().public())
        
    class Web:
        class IP:
            def local(self):
                return socket.gethostbyname(socket.gethostname())

            def public(self):
                try:
                    return requests.get("https://api.ipify.org").text
                except:
                    return None

        def hostname(self):
            return socket.gethostname()

        def mac(self):
            mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
            return ":".join([mac[e : e + 2] for e in range(0, 11, 2)])

        def network(self):
            return platform.node()

    class System:
        def name(self):
            return platform.system()

        def version(self):
            return platform.platform()

        def language(self):
            return locale.getlocale()[0]

        def encode(self):
            return locale.getlocale()[1]

        def release(self):
            return platform.release()

    class Processor:
        def info(self):
            return platform.processor() if platform.processor() else None

        def logic_count(self):
            return os.cpu_count()

    class Memory:
        def total(self):
            memory = psutil.virtual_memory()
            return f"{float(memory.total)/1024**3:.2f}GB"

        def used(self):
            memory = psutil.virtual_memory()
            return f"{float(memory.used)/1024**3:.2f}GB"

        def free(self):
            memory = psutil.virtual_memory()
            return f"{float(memory.free)/1024**3:.2f}GB"

        def available(self):
            memory = psutil.virtual_memory()
            return f"{float(memory.available)/1024**3:.2f}GB"

        def percent(self):
            memory = psutil.virtual_memory()
            return f"{round(memory.percent)}%"

    class Storage:
        def total(self, path):
            storage = shutil.disk_usage(path)
            return f"{storage.total/(1024**3):.2f}GB"

        def used(self, path):
            storage = shutil.disk_usage(path)
            return f"{storage.used/(1024**3):.2f}GB"

        def free(self, path):
            storage = shutil.disk_usage(path)
            return f"{storage.free/(1024**3):.2f}GB"

        def available(self, path):
            storage = psutil.disk_usage(path)
            return f"{storage.available/(1024**3):.2f}GB"

        def percent(self, path):
            storage = psutil.disk_usage(path)
            return f"{storage.percent}%"

    class Fps:
        def fps(self):
            start_time = time.time()
            end_time = 0
            fps = 0
            while not end_time - start_time >= 1:
                fps += 1
                end_time = time.time()
            return fps

    class Time:
        def timestamp(self):
            return time.time()

        def time_local(self):
            return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


device = Device()

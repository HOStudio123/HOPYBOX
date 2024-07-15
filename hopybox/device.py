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


class Device:
    def name(self):
        return platform.node()

    def type(self):
        return platform.machine()

    def bit(self):
        return platform.architecture()[0]

    def info(self):
        print(f"\033[95mOperating System\033[0m {platform.system()}")
        print(f"\033[95mOS Release\033[0m {platform.release()}")
        print(f"\033[95mOS Version\033[0m {platform.version()}")
        print(f"\033[95mMachine Type\033[0m {platform.machine()}")
        print(f"\033[95mProcessor\033[0m {Device().Processor().info()}")
        print(f"\033[95mCPU Count\033[0m {os.cpu_count()}")
        print(f"\033[95mNode Name\033[0m {platform.node()}")
        print(f"\033[95mLanguage\033[0m {locale.getlocale()[0]}")
        print(f"\033[95mEncode\033[0m {locale.getlocale()[1]}")
        print(f"\033[95mLocate IP\033[0m {Device().Web().IP().local()}")
        print(f"\033[95mPublic IP\033[0m {Device().Web().IP().public()}")

    class Web:
        class IP:
            def local(self):
                return socket.gethostbyname(socket.gethostname())

            def public(self):
                return requests.get("https://api.ipify.org").text

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

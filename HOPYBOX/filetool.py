import os
if os.name not in ['nt','java']:
  import pwd
  import grp
import time
from rich import console,syntax
from prompt_toolkit import prompt
from .prompt import error_cross
from .prompt import tip_tick
from .tree import tree

language_types = {
    ".py": "python",
    ".js": "javascript",
    ".java": "java",
    ".c": "c",
    ".cpp": "cpp",
    ".cs": "csharp",
    ".html": "html",
    ".css": "css",
    ".xml": "xml",
    ".sql": "sql",
    ".rb": "ruby",
    ".php": "php",
    ".swift": "swift",
    ".go": "go",
    ".rs": "rust",
    ".pl": "perl",
    ".ts": "typescript",
    ".kt": "kotlin",
    ".sh": "shell",
    ".ps1": "powershell",
    ".vb": "vbnet",
    ".m": "objc",
    ".r": "r",
    ".matlab": "matlab",
    ".asm": "asm",
    ".dart": "dart",
    ".scala": "scala",
    ".lua": "lua",
    ".groovy": "groovy",
    ".coffee": "coffeescript",
    ".lisp": "lisp",
    ".hs": "haskell",
    ".jl": "julia",
    ".erl": "erlang",
    ".clj": "clojure",
    ".fs": "fsharp",
    ".tcl": "tcl",
    ".pp": "puppet",
    ".awk": "awk",
    ".md": "markdown",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".ini": "ini",
    ".toml": "toml",
    ".diff": "diff",
    ".patch": "patch",
    ".gitmessage": "git",
    ".properties": "properties",
    ".cxx":"cpp",
    ".txt":"text"
}

Console = console.Console()

def f_time(timestamp):
  return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(timestamp))

def guess_encoding(path):
  encodings = ['UTF-8','ASCII','ISO-8859-1','UTF-16','UTF-16LE','UTF-16BE','UTF-32','UTF-32LE','UTF-32BE','GBK','GB2312','Big5','EUC-JP', 'Shift-JIS', 'EUC-KR', 'ISO-2022-JP', 'ISO-8859-2', 'ISO-8859-3','ISO-8859-4','ISO-8859-5','ISO-8859-6','ISO-8859-7','ISO-8859-8','ISO-8859-9','ISO-8859-10','ISO-8859-13','ISO-8859-14','ISO-8859-15','ISO-8859-16','windows-1250','windows-1251','windows-1252', 'windows-1253','windows-1254','windows-1255','windows-1256','windows-1257','windows-1258','KOI8-R','KOI8-U','MacRoman','IBM855', 'IBM866', 'IBM852', 'IBM857','IBM855', 'IBM862','IBM864','IBM869','IBM1026','TIS-620', 'TSCII','VISCII','TCVN-5712','PTCP154']
  for encoding in encodings:
    try:
      with open(path, 'r', encoding=encoding) as file:
        file.read(1024)
      return encoding
    except Exception:
      pass
  return None

class Filetool:
  def __init__(self,path):
    if os.path.isfile(r'%s' % path):
      self.path = path
      self.abspath = os.path.abspath(path)
    else:
      raise FileNotFoundError
  @property
  def info(self):
    print('\033[96m[Attribute]\033[0m')
    print(f'\033[92mName \033[0m\033[95m{self.name}\033[0m')
    print(f'\033[92mPath \033[0m\033[95m{self.abspath}\033[0m')
    print(f'\033[92mLanguage \033[0m\033[95m{self.lang}\033[0m')
    print(f'\033[92mEncoding \033[0m\033[95m{self.encoding}\033[0m')
    print(f'\033[92mPermission \033[0m\033[95m{self.permission_string} ({self.permission_code})\033[0m')
    print(f'\033[92mSize \033[0m\033[95m{self.size}\033[0m')
    print(f'\033[92mAccess time \033[0m\033[95m{self.a_time}\033[0m')
    print(f'\033[92mModification time \033[0m\033[95m{self.m_time}\033[0m')
    print(f'\033[92mOwner \033[0m\033[95m{self.owner}\033[0m')
    print(f'\033[92mUser \033[0m\033[95m{self.user}\033[0m')
  @property
  def view(self):
    if self.extension in language_types:
      file = open(self.path,'r',encoding=self.encoding)
    else:
      file = open(self.path,'rb')
    content = file.read()
    file.close()
    if self.extension in language_types:
      Console.print(syntax.Syntax(content,language_types[self.extension],theme='ansi_dark', line_numbers=True))
    else:
      print(content)
  @property
  def name(self):
    return os.path.basename(self.path)
  @property
  def extension(self):
    extension = os.path.splitext(self.path)[1]
    if extension != '':
      return extension
    else:
      return None
  @property
  def encoding(self):
    return guess_encoding(self.path)
  @property
  def size(self):
    try:
      return self._format_size(os.path.getsize(self.path))
    except:
      return None
  @property
  def lang(self):
    return language_types[self.extension] if self.extension in language_types else None
  @property
  def b_time(self):
    return f_time(os.path.getctime(self.path)) if os.name == 'nt' else '(No permission)'
  @property
  def m_time(self):
    return f_time(os.stat(self.path).st_mtime)
  @property
  def a_time(self):
    return f_time(os.stat(self.path).st_atime)
  @property
  def permission_code(self):
    return oct(os.stat(self.path).st_mode)[-3:]
  @property
  def owner(self):
    if os.name not in ['nt','java']:
      return pwd.getpwuid(os.stat(self.path).st_uid).pw_name
    return None
  @property
  def user(self):
    if os.name not in ['nt','java']:
      return grp.getgrgid(os.stat(self.path).st_gid).gr_name
    return None
  def _format_size(self,size):
    if size == None:
      return None
    num = 0
    while size > 1024:
      size /= 1024
      num += 1
    unit = ['B','KB','MB','GB','TB','PB']
    return f"{size:.2f} ".rstrip(".0").zfill(1)+unit[num]
  @property
  def permission_string(self):
    permissions = os.stat(self.path).st_mode
    owner_permissions = ''.join(['rwx'[i] if permissions >> (8 - i) & 0b001 else '-' for i in range(3)])
    group_permissions = ''.join(['rwx'[i] if permissions >> (5 - i) & 0b001 else '---'[i] for i in range(3)])
    other_permissions = ''.join(['rwx'[i] if permissions >> (2 - i) & 0b001 else '---'[i] for i in range(3)])
    return owner_permissions + group_permissions + other_permissions
    
filetool = Filetool

class Scanner:
  def __init__(self,path,extension):
    self.path = path
    self.extension = extension
    self.total_find = 0
    self.total_file = 0
  @property
  def scan_extension(self):
    with Console.status('\033[96mScanning files …\033[0m'):
      self._scan_dir(self.path)
    return f"\033[92m[Result]\033[0m\n\033[95mTotal files: {self.total_file}\nFiles with extension ({self.extension}): {self.total_find}"
  def _scan_dir(self,path):
    for item in os.listdir(path):
      full_path = os.path.join(path, item)
      if os.path.isdir(full_path):
        if os.access(full_path, os.R_OK):
          self._scan_dir(full_path)
      else:
        if os.path.isfile(full_path):
          self.total_file+=1
          extension = os.path.splitext(item)[1]
          if extension == self.extension:
            self.total_find+=1
            size = filetool(full_path).size
            print(f'\033[96m{full_path} ({size})\033[0m')
            
class Editingtool:
  def __init__(self):
    prompt('', multiline=True)

scanner = Scanner
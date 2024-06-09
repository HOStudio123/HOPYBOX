import os
import pwd
import grp
import time
import chardet
import zipfile
import tarfile
from rich import console,syntax
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
    print(f'\033[92mPermission \033[0m\033[95m{self.permission_string} ({self.permission_code})\033[0m')
    print(f'\033[92mCreated time \033[0m\033[95m{self.b_time}\033[0m')
    print(f'\033[92mSize \033[0m\033[95m{self.size}\033[0m')
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
      Console.print(syntax.Syntax(content,language_types[self.extension],theme='monokai', line_numbers=True))
    else:
      Console.print(syntax.Syntax(str(content),None,theme='monokai', line_numbers=True))
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
    try:
      file = open(self.path,'rb')
      return chardet.detect(file.read())['encoding']
    except:
      return None
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
  def permission_code(self):
    return oct(os.stat(self.path).st_mode)[-3:]
  @property
  def owner(self):
    return pwd.getpwuid(os.stat(self.path).st_uid).pw_name
  @property
  def user(self):
    return grp.getgrgid(os.stat(self.path).st_gid).gr_name
  def _format_size(self,size):
    num = 0
    while size > 1024:
      size /= 1024
      num += 1
    unit = ['B','KIB','MIB','GIB','TIB','PIB']
    return f"{size:.2f}".rstrip(".0").zfill(1)+unit[num]
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

scanner = Scanner
import os
import os.path
import filetype
import zipfile,tarfile
import time
from rich import console,syntax
from .hopter import Error_pta,Error_ptb,Tip_pta
from .tree_dir import tree_dir

def file_information(filename):
  print('''File-Size:{}B
File-Dev:{}
Fie-Nlink:{}
File-Ino:{}
File-Mtime:{}
File-Content:\033[0m'''.format(os.stat(filename).st_size,os.stat(filename).st_dev,os.stat(filename).st_nlink,os.stat(filename).st_ino,time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(os.stat(filename).st_mtime))))
  with console.Console().status("\033[96mLoading file …\033[0m"):
    file_open(filename)

def read_file(filename):
  if filename:
    try:
      filekind = filetype.guess(filename)
      if filekind is None:
        print('\033[92mFile-Type:text')
        mode = 'r'
        file_information(filename)
      else:
        file_type = filekind.extension
        print('\033[92mFile-Type:%s' % file_type)
        if file_type == 'png' or file_type == 'jpg':
          mode = 'rb'
          file_information(filename)
        elif file_type == 'zip':
          zip = zipfile.ZipFile(filename)
          print(zip.filename)
          for i in range(len(zip.namelist())):
            print('\033[94m├ '+zip.namelist()[i])
          unfile_answer = input('\033[94mDo you want to unzip to the current directory?(Y/n)')
          while True:
            if unfile_answer == 'Y' or unfile_answer == 'y':
              zip.extractall()
              Tip_pta('Extracted to the current directory')
              break
            elif unfile_answer == 'n':
              break
            else:
              Error_ptb(unfile_answer)
          else:
            pass
    except FileNotFoundError as e:
      Error_pta('FileNotFoundError','Command',str(e),'open '+filename)
    except UnicodeDecodeError as e:
      Error_pta('UnicodeDecodeError','Command',str(e),'open '+filename)
    except IsADirectoryError as e:
      Error_pta('IsADirectoryError','Command',str(e),'open '+filename)
    except PermissionError as e:
      Error_pta('PermissionError','Command',str(e),'open '+filename)
  else:
    Error_pta('FileNotFoundError','Command','Please enter a file name','open '+filename)

def file_open(filename):
  print('\033[92mFile-Content:\033[0m')
  Console = console.Console()
  file = open(filename,'rb')
  code = file.read().decode('utf-8')
  file.close()
  extension = os.path.splitext(filename)[1]
  if extension == '.py':
    Console.print(syntax.Syntax(code,'python',theme="ansi_dark", line_numbers=True))
  elif extension == '.html':
    Console.print(syntax.Syntax(code,'html',theme="ansi_dark", line_numbers=True))
  elif extension == '.c':
    Console.print(syntax.Syntax(code,'c',theme="ansi_dark", line_numbers=True))
  elif extension == '.cpp':
    Console.print(syntax.Syntax(code,'cpp',theme="ansi_dark", line_numbers=True))
  elif extension == '.java':
    Console.print(syntax.Syntax(code,'java',theme="ansi_dark", line_numbers=True))
  elif extension == '.sh':
    Console.print(syntax.Syntax(code,'bash',theme="ansi_dark", line_numbers=True))
  elif extension == '.js':
    Console.print(syntax.Syntax(code,'javascript',theme="ansi_dark", line_numbers=True))
  else:
    Console.print(syntax.Syntax(code,'text',theme="ansi_dark", line_numbers=True))

def del_file(filename):
  os.system('rm -rf '+filename)
  Tip_pta('successfully deleted')

def file_size(file):
  tree_dir(file)
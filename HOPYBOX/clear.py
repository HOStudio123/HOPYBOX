import os
import os.path
from .hopter import Error_pta,Tip_pta
from rich.console import Console

console = Console()

def clear_system(filename,extension,num=0,found_num=0):
  global scan_num,file_num,error
  scan_num = num
  file_num = found_num
  error = 0
  path = filename
  try:
    for item in os.listdir(path):
      scan_num+= 1
      file_extension = os.path.splitext(item)[1]
      if file_extension == extension:
        if os.path.isfile(path+'/'+item):
          file_num += 1
          print('\033[94;1m'+str(file_num)+'\033[0m','\033[95m'+path+'/'+item+'\033[0m','\033[92m(Scanned:'+str(scan_num)+')\033[0m')
          os.remove(path + '/' + item)
      new_item = path + '/' + item
      if os.path.isdir(new_item):
        clear_system(new_item,extension,scan_num,file_num)
  except Exception as e:
    Error_pta('CleanFilesError','Command',str(e),'clear …')
    error = 1

def clear(filename,extension):
  global scan_num,file_num,error
  with console.status("\033[96mCleaning files …\033[0m"):
    clear_system(filename,extension)
  if not error:
    Tip_pta('Clear is complete, a total of scan {} file, clear {} target file'.format(scan_num,file_num))
    error = 0
import os
import os.path
from .hopter import Error_pta,Tip_pta
from rich.console import Console

console = Console()

file_apk_num = 0 # Number of installation packets
file_pic_num = 0 # Picture number
file_exe_num = 0 # Executable number
file_vid_num = 0 # Audio video

# Format list
list_aip = ['.apk','.xapk','.ipa','.pxl','.deb','.sis','.sisx','.xap']
list_exe = ['.exe','.bat','.sys','.com']
list_pic = ['.png','.jpg','.svg','.gif','.dif','.dip','.jpeg','.eps']
list_vid = ['.wmv','.asf','.asx','.mp3','.mp4','.amc','.dat','.m4v','.wav']

def scan_system(filename,extension,num=0,found_num=0):
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
        file_num+=1
        if os.path.isfile(path+'/'+item):
          print('\033[94;1m'+str(file_num)+'\033[0m','\033[95m'+path+'/'+item+'\033[0m','\033[92m(Scanned:'+str(scan_num)+')\033[0m')
        else:
          print('\033[94;1m'+str(file_num)+'\033[0m','\033[96m'+path+'/'+item+'\033[0m','\033[92m(Scanned:'+str(scan_num)+')\033[0m')
      new_item = path + '/' + item
      if os.path.isdir(new_item):
        scan_system(new_item,extension,scan_num,file_num)
  except Exception as e:
    Error_pta('ScanFilesError','Command',str(e),'scan …')
    error = 1

def scan(filename,extension):
  global scan_num,file_num,error
  with console.status("\033[96mScanning files …\033[0m"):
    scan_system(filename,extension)
  if not error:
    Tip_pta('Scan is complete, a total of scan {} file, discover {} target file'.format(scan_num,file_num))
  error = 0

def scan_all(filename):
  global scan_num,file_apk_num,file_pic_num,file_exe_num,file_vid_num,error
  with console.status("\033[96mScanning files …\033[0m"):
    scan_all_system(filename)
  if not error:
    Tip_pta('Scan is complete, a total of scan {} file, Below is the scan result:'.format(scan_num))
    print('\033[95m\nApplication installation package:{}\nExecutable file:{}\n'.format(file_apk_num,file_exe_num))
  error = 0
  
def scan_all_system(filename,num=0,found_num=0):
  global scan_num,file_apk_num,file_pic_num,file_exe_num,file_vid_num,error
  scan_num = num
  file_num = found_num
  error = 0
  path = filename
  try:
    for item in os.listdir(path):
      scan_num+= 1
      file_extension = os.path.splitext(item)[1]
      if file_extension in list_aip:
        file_apk_num+= 1
        file_num+= 1
        if os.path.isfile(path+'/'+item):
          print('\033[94;1m'+str(file_num)+'\033[0m','\033[95m'+path+'/'+item+'\033[0m','\033[92m(Scanned:'+str(scan_num)+')\033[0m')
        else:
          print('\033[94;1m'+str(file_num)+'\033[0m','\033[96m'+path+'/'+item+'\033[0m','\033[92m(Scanned:'+str(scan_num)+')\033[0m')
      elif file_extension in list_exe:
        file_exe_num+= 1
        file_num+= 1
        if os.path.isfile(path+'/'+item):
          print('\033[94;1m'+str(file_num)+'\033[0m','\033[95m'+path+'/'+item+'\033[0m','\033[92m(Scanned:'+str(scan_num)+')\033[0m')
        else:
          print('\033[94;1m'+str(file_num)+'\033[0m','\033[96m'+path+'/'+item+'\033[0m','\033[92m(Scanned:'+str(scan_num)+')\033[0m')
      elif file_extension in list_exe:
        file_pic_num+= 1
        file_num+= 1
        if os.path.isfile(path+'/'+item):
          print('\033[94;1m'+str(file_num)+'\033[0m','\033[95m'+path+'/'+item+'\033[0m','\033[92m(Scanned:'+str(scan_num)+')\033[0m')
        else:
          print('\033[94;1m'+str(file_num)+'\033[0m','\033[96m'+path+'/'+item+'\033[0m','\033[92m(Scanned:'+str(scan_num)+')\033[0m')
      elif file_extension in list_vid:
        file_vid_num+= 1
        file_num+= 1
        if os.path.isfile(path+'/'+item):
          print('\033[94;1m'+str(file_num)+'\033[0m','\033[95m'+path+'/'+item+'\033[0m','\033[92m(Scanned:'+str(scan_num)+')\033[0m')
        else:
          print('\033[94;1m'+str(file_num)+'\033[0m','\033[96m'+path+'/'+item+'\033[0m','\033[92m(Scanned:'+str(scan_num)+')\033[0m')
      new_item = path + '/' + item
      if os.path.isdir(new_item):
        scan_all_system(new_item,scan_num,file_num)
  except Exception as e:
    Error_pta('ScanFilesError','Command',str(e),'scan …')
    error = 1
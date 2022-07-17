import sys
from platform import system,python_version

version_number = 165
version_code = '1.6.5
version_type = 'default'
# version_type = 'Beta'
try:
  gcc_version = sys.version.split(' ')[8].split(']')[0]
except:
  gcc_version = 'Failed'

head_version = 'HOPYBOX {} ({}, July 9 2022, 13:10:11)\n[Python {}] on {}\nType "help" , "copyright" , "version" , "update" or "license" for more information'.format(version_code,version_type,python_version(),system())

def system_version():
  print('\033[96mHOPYBOX:{}\nPython:{}\nGCC:{}'.format(version_code,python_version(),gcc_version))
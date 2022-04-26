import os
def systems(order):
  print('\033[36;1m',end='\r')
  os.system(order)
def runpy(module):
  print('\033[0m',end='\r')
  os.system('python '+module)
def python():
  os.system('python')
def install(modules):
  print('\033[36;m',end='\r')
  os.system('python3 -m pip3 install -U {}'.format(modules))
def uninstall(modules):
  print('\033[36;m',end='\r')
  os.system('python3 -m pip3 uninstall {}'.format(modules))
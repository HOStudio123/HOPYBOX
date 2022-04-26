def all_help():
  print('''\033[32m1.Help
├ help 
└ help <module> 
2.Id
└ id <text> 
3.Runpy
└ run <file> 
4.Last
└ If you have any questions, please contact the developer as 479571968@qq.com ''')
def module_help(module):
  print('\033[32m',end='\r')
  print(help(module))
from ho_logs import *
def error_a(error,pattern,text,value):
  print("\033[0m\033[31;1m× {} in {} '{}':\n╰─ {}  ".format(error,pattern,value,text))
  wlog(value,"× {} in {} '{}':\n╰─ {}  ".format(error,pattern,value,text))
def error_b(text,anwer):
  print('\033[32;1m{}:Your response (\'{}\') was not one of the expected responses: y, n Proceed (Y/n)?'.format(text,anwer))
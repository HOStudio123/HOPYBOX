def Error_pta(error,pattern,text,value):
  print("\033[31m× {} in {} '{}':\n╰─ {}  ".format(error,pattern,value,text))
def Error_ptb(text,anwer):
  print('\033[32m{}:Your response (\'{}\') was not one of the expected responses: y, n Proceed (Y/n)?'.format(text,anwer))
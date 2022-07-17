## Error type printing

# Basic error reporting
def Error_pta(error,pattern,text,value):
  print("\033[91m✗ {} in {} '{}':\n╰─ {}  ".format(error,pattern,value,text))

# Enter is not what the program wants
def Error_ptb(answer):
  result = input('\033[93mYour response (\'{}\') was not one of the expected responses: y, n Proceed (Y/n)?'.format(answer))
  return results

def Error_ptc(text,error):
  print('\033[91mE:{},Because {}.\033[0m'.format(text,error))

## Some simple tips
def Tip_pta(text):
  print('\033[92m✓ \033[0m\033[96m {}'.format(text))
  
def Tip_ptb(text):
  print('\033[92m➤ \033[0m\033[96m {}'.format(text))
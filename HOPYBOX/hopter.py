# Basic error reporting
def Error_pta(error,pattern,text,value):
  print("\033[91m✗ {} in {} '{}':\n╰─ {}  ".format(error,pattern,value,text))

# Enter is not what the program wants
def Error_ptb(answer):
  result = input('\033[93mYour response (\'{}\') was not one of the expected responses: y, n Proceed (Y/n)?'.format(answer))
  return results

# Some simple tips
def Tip_pta(text): # tick | need change name
  print('\033[92m✓ \033[0m\033[96m {}'.format(text))
  
  
# New

def error_cross(error,mode,text,value): # cross
  print(f"\033[91m✗ {error} in {mode} '{value}':\n╰─ {text}  ")

def tip_arrow(text): # arrow
  print(f'\033[92m➤ \033[0m\033[96m {text}')

def tip_tick(text): # tick
  print(f'\033[92m✓ \033[0m\033[96m {text}')
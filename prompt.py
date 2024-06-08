def ask_proceed(question): # question
  answer = input(f'\033[92m➤ \033[0m\033[96m  {question} , Do you want to proceed ? (Y/n) \033[0m')
  if answer in ['Y','y','']:
    return True
  elif answer in ['N','n']:
    return False
  else:
    print(f"\033[31m✗ Your response('{answer}') was not one of the expected responses: y, n\033[0m")
    return None

def error_cross(error,mode,text,value): # cross
  print(f"\033[91m✗ {error} in {mode}: \n '{value}' -> {text} \033[0m")

def tip_tick(text): # tick
  print(f'\033[92m✓ \033[0m\033[96m {text}\033[0m')
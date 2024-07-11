'''
Copyright (c) 2022-2024 HOStudio123(ChenJinlin).
All Rights Reserved.
'''

#!/usr/bin/env python3

# -*- coding:utf-8 -*-

import sys
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

reset = '\033[0m'

def ask_proceed(question): # question
  answer = input(f'\033[92m➤ \033[0m\033[96m  {question} , Do you want to proceed ? (Y/n) \033[0m')
  if answer in ['Y','y','']:
    return True
  elif answer in ['N','n']:
    return False
  else:
    print(f"\033[31m✗ Your response('{answer}') was not one of the expected responses: y, n{reset}")
    return None

def error_cross(error,mode,text,value): # cross
  print(f"\033[91m✗ {error} in {mode}: \n '{value}' -> {text}{reset}")

def tip_tick(text): # tick
  print(f'\033[92m✓ \033[96m {text}{reset}')

def getpass(text,color): # password
  style = Style.from_dict({'prompt':color})
  return prompt(text,is_password=True,style=style)
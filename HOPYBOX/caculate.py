import math
import cmath
from .hopter import Error_pta

# Ordinary calculations

def caculate(num):
  num_logos = ['+','-','*','/','%','|','&','^','~','>>','<<']
  for i in num_logos:
    if i in num:
      try:
        print('\033[92m'+str(eval(num)))
      except SyntaxError as e:
        Error_pta('SyntaxError','Command',str(e),num)
      except ZeroDivisionError as e:
        Error_pta('ZeroDivisonError','Command',str(e),num)
    else:
      try:
        print('\033[92m'+str(eval(num)))
      except SyntaxError as e:
        Error_pta('SyntaxError','Command',str(e),num)
      except NameError as e:
        Error_pta('NameError','Command',str(e),num)
      except UnicodeEncodeError as e:
        Error_pta('UnicodeEncodeError','Command',str(e),num)
    break

# Root number calculation

def root_caculate(num):
  try:
    if float(num) >= 0:
      print('\033[92m'+str(math.sqrt(float(num))))
    else:
      print('\033[92m'+str(cmath.sqrt(float(num))))
  except SyntaxError as e:
    Error_pta('SyntaxError','Command',str(e),'caculate √'+num)
  except ValueError as e:
    Error_pta('ValueError','Command',str(e),'caculate √'+num)
  except UnicodeEncodeError as e:
    Error_pta('UnicodeEncodeError','Command',str(e),'caculate √'+num)

#Absolute value calculation

def abs_caculate(num):
  try:
    print('\033[92m'+str(abs(float((num[:len(num)-1])))))
  except SyntaxError as e:
    Error_pta('SyntaxError','Command',str(e),'caculate |{}|'.format(num[:len(num)-1]))
  except ValueError as e:
    Error_pta('ValueError','Command',str(e),'caculate |{}|'.format(num[:len(num)-1]))
  except UnicodeEncodeError as e:
    Error_pta('UnicodeEncodeError','Command',str(e),'caculate |{}|'.format(num[:len(num)-1]))

#Trigonometric computation

def triangle_caculate(nums):
  symbol = ['sin','cos','tan','asin','acos','atan']
  for type in range(len(symbol)):
    if symbol[type] in nums:
      num = nums[len(symbol[type]):]
      break
  try:
    if type == 0:
      print('\033[92m'+str(math.sin(math.radians(float(num)))))
    elif type == 1:
      print('\033[92m'+str(math.cos(math.radians(float(num)))))
    elif type == 2:
      print('\033[92m'+str(math.tan(math.radians(float(num)))))
    elif type == 3:
      print('\033[92m'+str(math.asin(math.radians(float(num)))))
    elif type == 4:
      print('\033[92m'+str(math.acos(math.radians(float(num)))))
    elif type == 5:
      print('\033[92m'+str(math.atan(math.radians(float(num)))))
  except SyntaxError as e:
    Error_pta('SyntaxError','Command',str(e),'triangle …')
  except UnboundLocalError as e:
    Error_pta('UnboundLocalError','Command',str(e),'triangle …')
  except ValueError as e:
    Error_pta('ValueError','Command',str(e),'triangle …')
  except UnicodeEncodeError as e:
    Error_pta('UnicodeEncodeError','Command',str(e),'triangle …')

#Other calculations

def pi_print():
  print('\033[92m'+str(math.pi))
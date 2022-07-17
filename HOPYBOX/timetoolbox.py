import time

def timestamp_print():
  print('\033[92m'+str(time.time()))
  
def timestamp():
  return time.time()

def format_time_a():
  return time.strftime("%H:%M:%S",time.localtime(timestamp()))

def format_time_a_print():
  print('\033[92m'+time.strftime("%H:%M:%S",time.localtime(timestamp())))
  
def format_time_b_print():
  print('\033[92m'+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(timestamp())))
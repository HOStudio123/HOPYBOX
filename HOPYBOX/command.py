command_data = dict()

def _command_add(mode,name,code,operate,details):
  if mode in command_data:
    command_data[mode][name] = {'code':code,'help':{'operate':operate,'details':details}}
  else:
    command_data[mode] = {name:{'code':code,'help':{'operate':operate,'details':details}}}

def command_data_add():
  _command_add('Program','help',"if 'run' in command_data[_mode]['help']:\n  print(command_help(_mode,command_data[_mode]['help']['run']))\nelse:\n  print(command_help(_mode,'help'))",'help {command}','Type help {command} for help about command')
  _command_add('Program','exit','exit()','exit','Exit the program')
  _command_add('Program','clear','clear()','clear','Clear console')
  _command_add('Program','switch',"_switch(command_data['Program']['switch']['run'])",'switch {mode}','To switch program mode')
  _command_add('Device','help',"if command_data[_mode]['help']['run']:\n  print(command_help(_mode,command_data[_mode]['help']['run']))\nelse:\n  print(command_help(_mode,'help'))",'help {command}','Type help {command} for help about command')
  _command_add('Device','exit','exit()','exit','Exit the program')
  _command_add('Device','clear','clear()','clear','Clear console')
  _command_add('Device','switch',"_switch(command_data['Device']['switch']['run'])",'switch {mode}','To switch program mode')
  # Program _command_add('Program','','','','')
  _command_add('Program','hoget',"hoget.main(command_data['Program']['hoget']['run'])",'hoget {URL}','To access website addresses')
  _command_add('Program','browser',"browser(command_data['Program']['browser']['run'])",'browser {URL}','Initiate your browser and visit url')
  _command_add('Program','uplog',"update_log_get(command_data['Program']['uplog']['run'])",'uplog {version}','To get a update log about the version object')
  _command_add('Program','terminal',"terminal('sh')",'terminal','Entering the system terminal')
  _command_add('Program','author','print(__author__)','author','Learn about program developer name')
  _command_add('Program','copyright','print(__copyright__)','copyright','Learn about program copyright')
  _command_add('Program','version','print(_version_all)','version','Learn about program version')
  _command_add('Program','update','update_program()','update','To update the version')
  _command_add('Program','license',"print(license())",'license','To view the license')
  _command_add('Program','feedback',"print('\033[96mIf you have any questions or suggestions, please contact the developer as\033[0m\033[1;95m hostudio.hopybox@foxmail.com')",'feedback','To get the way of feedback')
  _command_add('Program','trans',{'-y':'translate.YouDao().trans(par_t,char(par_t)[1])'},[],[])
  # Device _command_add('Device','','','','')
  _command_add('Device','name','print(device.name())','name','To get the device name')
  _command_add('Device','type','print(device.type())','name','To get the device type')
  _command_add('Device','ip',{'-l':'print(device.Web().IP().local())','-p':'print(device.Web().IP().public())'},['ip -l','ip -p'],['To get the local ip address','To get the public ip address'])
  _command_add('Device','system',{'-n':'print(device.System().name())','-v':'print(device.System().version())','-l':'print(device.System().language())','-e':'print(device.System().encode())'},['system -n','system -v','system -l','system -e'],['To get the system name','To get the system version','To get the system language','To get the system encode'])
  _command_add('Device','mac','print(device.Web().mac())','mac','To get the device mac')
  _command_add('Device','fps','print(device.Fps().fps())','fps','To get the device fps')
  _command_add('Device','timestamp','print(device.Time().timestamp())','timestamp','To get the device timestamp')
  _command_add('Device','time','print(device.Time().time_local())','time','To get the local time')
def par(mode,command):
  return command_data[mode][command]['run']

def command_help(mode,command):
  record = ''
  if type(command_data[mode][command]['help']['operate'])!=type('string'):
    for i in range(len(command_data[mode][command]['help']['operate'])):
      operate = command_data[mode][command]['help']['operate'][i]
      details = command_data[mode][command]['help']['details'][i]
      record+=f"\033[94mUsage\033[0m {operate}\n\033[94mDescription\033[0m {details}"
      if i+1 < len(command_data[mode][command]['help']['operate']):
        record+='\n'
      i+=1
    return record
  else:
    return f"\033[94mUsage\033[0m {command_data[mode][command]['help']['operate']}\n\033[94mDescription\033[0m {command_data[mode][command]['help']['details']}"
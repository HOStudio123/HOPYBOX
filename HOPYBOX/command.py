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
  _command_add('Program','switch',"_switch(command_data['Program']['switch']['run'])",'switch {mode}','To switch running mode')
  _command_add('Device','help',"if command_data[_mode]['help']['run']:\n  print(command_help(_mode,command_data[_mode]['help']['run']))\nelse:\n  print(command_help(_mode,'help'))",'help {command}','Type help {command} for help about command')
  _command_add('Device','exit','exit()','exit','Exit the program')
  _command_add('Device','clear','clear()','clear','Clear console')
  _command_add('Device','switch',"_switch(command_data['Device']['switch']['run'])",'switch {mode}','To switch running mode')
  _command_add('Calculate','help',"if 'run' in command_data[_mode]['help']:\n  print(command_help(_mode,command_data[_mode]['help']['run']))\nelse:\n  print(command_help(_mode,'help'))",'help {command}','Type help {command} for help about command')
  _command_add('Calculate','exit','exit()','exit','Exit the Calculate')
  _command_add('Calculate','clear','clear()','clear','Clear console')
  _command_add('Calculate','switch',"_switch(command_data['Calculate']['switch']['run'])",'switch {mode}','To switch running mode')
  _command_add('File','help',"if 'run' in command_data[_mode]['help']:\n  print(command_help(_mode,command_data[_mode]['help']['run']))\nelse:\n  print(command_help(_mode,'help'))",'help {command}','Type help {command} for help about command')
  _command_add('File','exit','exit()','exit','Exit the File')
  _command_add('File','clear','clear()','clear','Clear console')
  _command_add('File','switch',"_switch(command_data['File']['switch']['run'])",'switch {mode}','To switch running mode')
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
  _command_add('Program','feedback',"print('\033[96mIf you have any questions or suggestions, please contact the developer as\033[0m\033[4;95m hostudio.hopybox@foxmail.com')",'feedback','To get the way of feedback')
  _command_add('Program','email',"email(command_data['Program']['email']['run'])",'email {mail}','Send emails to people')
  _command_add('Program','translate',{'-y':"translate.YouDao().output(translate.YouDao().trans(command_data['Program']['translate']['run'],char(command_data['Program']['translate']['run'])[1]))",'-g':"print(translate.Google().trans(command_data['Program']['translate']['run'],char(command_data['Program']['translate']['run'])[1]))"},['translate -y {text}','translate -g {text}'],['To translate the word into Chinese/English by YouDao','To translate the word into Chinese/English by Google'])
  # Device _command_add('Device','','','','')
  _command_add('Device','name','print(device.name())','name','To get the device name')
  _command_add('Device','type','print(device.type())','type','To get the device type')
  _command_add('Device','bit','print(device.bit())','bit','To get the device bit')
  _command_add('Device','ip',{'-l':'print(device.Web().IP().local())','-p':'print(device.Web().IP().public())'},['ip -l','ip -p'],['To get the local ip address','To get the public ip address'])
  _command_add('Device','system',{'-n':'print(device.System().name())','-v':'print(device.System().version())','-l':'print(device.System().language())','-e':'print(device.System().encode())','-r':'print(device.System().release())'},['system -n','system -v','system -l','system -e','system -r'],['To get the system name','To get the system version','To get the system language','To get the system encode','To get the system release'])
  _command_add('Device','mac','print(device.Web().mac())','mac','To get the device mac')
  _command_add('Device','fps','print(device.Fps().fps())','fps','To get the device fps')
  _command_add('Device','network','print(device.Web().name())','network','To get the name of device network')
  _command_add('Device','hostname','print(device.Web().hostname())','hostname','To get the device hostname')
  _command_add('Device','timestamp','print(device.Time().timestamp())','timestamp','To get the device timestamp')
  _command_add('Device','time','print(device.Time().time_local())','time','To get the local time')
  # Calculate _command_add('Calculate','','','','')
  _command_add('Calculate','triangle',{'-a':"print(calculate.Triangle(float(command_data['Calculate']['triangle']['run'].split(' ')[0]),float(command_data['Calculate']['triangle']['run'].split(' ')[1]),float(command_data['Calculate']['triangle']['run'].split(' ')[2])).area)",'-p':"print(calculate.Triangle(float(command_data['Calculate']['triangle']['run'].split(' ')[0]),float(command_data['Calculate']['triangle']['run'].split(' ')[1]),float(command_data['Calculate']['triangle']['run'].split(' ')[2])).perimeter)"},['triangle -a {a} {b} {c}','triangle -p {a} {b} {c}'],['To calculate area','To calculate perimeter'])
  _command_add('Calculate','circle',{'-a':"print(calculate.Circle(float(command_data['Calculate']['circle']['run'])).area)",'-p':"print(calculate.Circle(float(command_data['Calculate']['circle']['run'])).perimeter)",'-d':"print(calculate.Circle(float(command_data['Calculate']['circle']['run'])).diameter)"},['circle -a {radius}','circle -p {radius}','circle -d {radius}'],['To calculate area','To calculate perimeter','To calculate diameter'])
  # File _command_add('File','','','','')
  _command_add('File','workpath','print(os.getcwd())','workpath','To get the work path')
  _command_add('File','tree',"tree(command_data['File']['tree']['run'])",'tree {path}','Drawing the file tree directory')
  _command_add('File','open',"filetool(command_data['File']['open']['run']).view",'open {path}','Viewing the content of file')
  _command_add('File','info',"filetool(command_data['File']['info']['run']).info",'info {path}','Viewing the content of file')
  _command_add('File','scan',"print(scanner(command_data['File']['scan']['run'].split(' ')[0],command_data['File']['scan']['run'].split(' ')[1]).scan_extension)",'scan {path} {extension}','Scanning the path')

def command_help(mode,command):
  record = ''
  if type(command_data[mode][command]['help']['operate'])!=str:
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
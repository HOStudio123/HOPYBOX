command_data = dict()

def _command_add(mode,name,code,operate,details):
  if mode in command_data:
    command_data[mode][name] = {'code':code,'help':{'operate':operate,'details':details}}
  else:
    command_data[mode] = {name:{'code':code,'help':{'operate':operate,'details':details}}}

def command_data_add():
  _command_add('Key','Control',None,['Control-C','Control-D'],['Enable or exit mouse mode','Exit the program'])
  _command_add('Global','help',"if 'run' in command_data['Global']['help']:\n  print(command_help(_mode,command_data['Global']['help']['run']))\nelse:\n  command_help(None,None)",'help {command}','Type "help {command}" for help about this command or "help" for help about all commands')
  _command_add('Global','exit','exit()','exit','Exit the program')
  _command_add('Global','clear','clear()','clear','Clear console')
  _command_add('Global','switch',"_switch(command_data['Global']['switch']['run'])",'switch {mode}','To switch running mode')
  # Program _command_add('Program','','','','')
  _command_add('Program','hoget',"hoget.main(command_data['Program']['hoget']['run'])",'hoget {URL}','To access website addresses')
  _command_add('Program','browser',"browser(command_data['Program']['browser']['run'])",'browser {URL}','Initiate your browser and visit url')
  _command_add('Program','uplog',"update_log_get(command_data['Program']['uplog']['run'])",'uplog {version}','To get a update log about the version object, type "uplog all" can view all the update log')
  _command_add('Program','terminal',"terminal('sh')",'terminal','Entering the system terminal')
  _command_add('Program','author','print(__author__)','author','Learn about program developer name')
  _command_add('Program','copyright','print(__copyright__)','copyright','Learn about program copyright')
  _command_add('Program','version','print(_version_all)','version','Learn about program version')
  _command_add('Program','update','update_program()','update','To update the version')
  _command_add('Program','license',"print(license())",'license','To view the license')
  _command_add('Program','feedback',"print('\033[96mIf you have any questions or suggestions, please contact the developer as\033[0m\033[4;95m hostudio.hopybox@foxmail.com')",'feedback','To get the way of feedback')
  _command_add('Program','email',"email()",'email','Send emails to people')
  _command_add('Program','totp',{'-s':"totp.set()",'-v':"totp.display()",'-d':"totp.delete()"},['totp -s','totp -v','totp -d'],['To set the 2FA key','To view the 2FA token','To delete the 2FA key'])
  _command_add('Program','translate',{'-y':"translate.YouDao().output(translate.YouDao().trans(command_data['Program']['translate']['run'],langdet(command_data['Program']['translate']['run'])[1]))",'-g':"print(translate.Google().trans(command_data['Program']['translate']['run'],langdet(command_data['Program']['translate']['run'])[1]))"},['translate -y {text}','translate -g {text}'],['To translate the word into Chinese/English by YouDao','To translate the word into Chinese/English by Google'])
  _command_add('Program','download',"download(command_data['Program']['download']['run'])",'download','To get the way of feedback')
  _command_add('Program','hopybox',"print(hopybox_artword)",'hopybox','To get the wordart of hopybox')
  # Device _command_add('Device','','','','')
  _command_add('Device','name','print(device.name())','name','To get the device name')
  _command_add('Device','type','print(device.type())','type','To get the device type')
  _command_add('Device','bit','print(device.bit())','bit','To get the device bit')
  _command_add('Device','info','device.info()','info','To get the device info')
  _command_add('Device','ip',{'-l':'print(device.Web().IP().local())','-p':'print(device.Web().IP().public())'},['ip -l','ip -p'],['To get the local ip address','To get the public ip address'])
  _command_add('Device','system',{'-n':'print(device.System().name())','-v':'print(device.System().version())','-l':'print(device.System().language())','-e':'print(device.System().encode())','-r':'print(device.System().release())'},['system -n','system -v','system -l','system -e','system -r'],['To get the system name','To get the system version','To get the system language','To get the system encode','To get the system release'])
  _command_add('Device','processor',{'-i':'print(device.Processor().info())','-l':'print(device.Processor().logic_count())','-c':'print(device.Processor().core_count())'},['processor -i','processor -l','processor -c'],['To get the processor info','To get the cpu logic count','To get the cpu core count'])
  _command_add('Device','mac','print(device.Web().mac())','mac','To get the device mac')
  _command_add('Device','fps','print(device.Fps().fps())','fps','To get the device fps')
  _command_add('Device','network','print(device.Web().network())','network','To get the name of device network')
  _command_add('Device','hostname','print(device.Web().hostname())','hostname','To get the device hostname')
  _command_add('Device','timestamp','print(device.Time().timestamp())','timestamp','To get the device timestamp')
  _command_add('Device','time','print(device.Time().time_local())','time','To get the local time')
  _command_add('Device','storage',{'-t':"print(device.Storage().total(command_data['Device']['storage']['run']))",'-u':"print(device.Storage().used(command_data['Device']['storage']['run']))",'-f':"print(device.Storage().free(command_data['Device']['storage']['run']))",'-p':"print(device.Storage().percent(command_data['Device']['storage']['run']))",'-a':"print(device.Storage().available(command_data['Device']['storage']['run']))"},['storage -t {dir}','storage -u {dir}','storage -f {dir}','storage -p {dir}','storage -a {dir}'],['Used to get the total amount of storage','Used to get the storage occupied','Used to get the remaining amount of storage','Used to get the percentage of storage occupied','Used to get the memory available'])
  _command_add('Device','memory',{'-t':"print(device.Memory().total())",'-u':"print(device.Memory().used())",'-f':"print(device.Memory().free())",'-p':"print(device.Memory().percent())",'-a':"print(device.Memory().available())"},['memory -t','memory -u','memory -f','memory -p','memory -a'],['Used to get the total amount of memory','Used to get the memory occupied','Used to get the remaining amount of memory','Used to get the percentage of memory occupied','Used to get the memory available'])
  # Calculate _command_add('Calculate','','','','')
  _command_add('Calculate','!',"print(calculate.Expression().run(command_data['Calculate']['!']['run']))",'! {expression}','Used by calculate')
  _command_add('Calculate','dx',{'-d':"print(calculate.Function(command_data['Calculate']['dx']['run'][1]).derivative(command_data['Calculate']['dx']['run'][0]))"},'dx {level} {function}','Used by differentiation')
  _command_add('Calculate','triangle',{'-a':"print(calculate.Triangle(float(command_data['Calculate']['triangle']['run'][0]),float(command_data['Calculate']['triangle']['run'][1]),float(command_data['Calculate']['triangle']['run'][2])).area)",'-p':"print(calculate.Triangle(float(command_data['Calculate']['triangle']['run'][0]),float(command_data['Calculate']['triangle']['run'][1]),float(command_data['Calculate']['triangle']['run'][2])).perimeter)"},['triangle -a {a} {b} {c}','triangle -p {a} {b} {c}'],['To calculate area','To calculate perimeter'])
  _command_add('Calculate','circle',{'-a':"print(calculate.Circle(float(command_data['Calculate']['circle']['run'])).area)",'-p':"print(calculate.Circle(float(command_data['Calculate']['circle']['run'])).perimeter)",'-d':"print(calculate.Circle(float(command_data['Calculate']['circle']['run'])).diameter)"},['circle -a {radius}','circle -p {radius}','circle -d {radius}'],['To calculate area','To calculate perimeter','To calculate diameter'])
  # File _command_add('File','','','','')
  _command_add('File','workdir','print(os.getcwd())','workdir','To get the work path')
  _command_add('File','home',"print(os.path.expanduser('~'))",'workdir','To get the home path')
  _command_add('File','tree',"tree(command_data['File']['tree']['run'])",'tree {dir}','Drawing the file tree directory')
  _command_add('File','open',"filetool(command_data['File']['open']['run']).view",'open {path}','To view the content of file')
  _command_add('File','info',"filetool(command_data['File']['info']['run']).info",'info {path}','To view the information of file')
  _command_add('File','scan',"print(scanner(command_data['File']['scan']['run'][0],command_data['File']['scan']['run'][1]).scan_extension)",'scan {path} {extension}','Scanning the path')
  _command_add('File','chdir',"os.chdir(command_data['File']['chdir']['run'])\ntip_tick('The working directory is switched successfully')",'chdir {path}','To switch the work path')
  _command_add('File','worklist','tree(os.getcwd())','worklist','To get the work dir list')
  _command_add('File','mkdir',"os.mkdir(command_data['File']['mkdir']['run'])",'mkdir {dir}','To create a dir')
  _command_add('File','remove',{'-f':"os.remove(command_data['File']['remove']['run'])",'-d':"os.rmdir(command_data['File']['remove']['run'])"},['remove -f {path}','remove -d {dir}'],['To remove the file','To remove the dir'])

def command_help(mode,command):
  record = ''
  if command in command_data['Global']:
    mode = 'Global'
  if command == None and mode == None:
    for m in command_data:
      print(f'\033[92m[{m}]\033[0m',end=' ')
      if m not in ['Global','Key']:
        print(f'\033[95m(Type "switch {m}" to enter the mode)\033[0m')
      else:
        print()
      for c in command_data[m]:
        if type(command_data[m][c]['help']['operate'])!=str:
          for i in range(len(command_data[m][c]['help']['operate'])):
            operate = command_data[m][c]['help']['operate'][i]
            details = command_data[m][c]['help']['details'][i]
            print(f"\033[94mUsage\033[0m {operate}\n\033[94mDescription\033[0m {details}")
        else:
          print(f"\033[94mUsage\033[0m {command_data[m][c]['help']['operate']}\n\033[94mDescription\033[0m {command_data[m][c]['help']['details']}")
  elif type(command_data[mode][command]['help']['operate'])!=str:
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
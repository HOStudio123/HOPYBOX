from .prompt import color_print

command_data = dict()

def _command_add(mode, name, code, operate, details):
    if mode in command_data:
        command_data[mode][name] = {
            "code": code,
            "help": {
                "operate": operate, 
                "details": details
                },
        }
    else:
        command_data[mode] = {
            name: {
            "code": code, 
            "help": {
                "operate": operate, 
                "details": details
                }
            }
        }


def command_data_add():
    # Key
    Key = [
    ("Ctrl+C",None,'^C',"Continue the conversation"),
    ("Ctrl+D",None,'^D',"Exit the program")
    ]
    
    # Global
    Global = [
    ("help","command_help()",'help [command]','To get the help about all commands'),
    
    ("switch","_switch(command_data['Global']['switch']['run'])","switch [program|device|file|calculate]","To switch running mode"),
    
    ("clear","clear()","clear","Clear console"),
    
    ("exit","exit()","exit","Exit the program")
    ]
    
    # Program
    Program = [
    ("hopybox","color_print(hopybox_artword,'#00FFFF')","hopybox","To get the wordart of hopybox"),
    
    ("hoget","hoget.main(command_data['Program']['hoget']['run'])","hoget [URL]","To access website addresses"),
    
    ("browser","browser(command_data['Program']['browser']['run'])","browser [URL]","Initiate your browser and visit url"),
    
    ("coral","coral._chat","coral","Chat with Coral"),
    
    ("color","color(command_data['Program']['color']['run'])","color [#(code)]","Returns the color represented by the color code"),
    
    ("uplog","update_log_format(_version_code,_version_update_time,_version_update_content)","uplog [version]","To get a update log about the latest version"),
    
    ("version","color_print(_version_info,'#FF00FF')","version","Learn about program version"),
    
    ("copyright","print(__copyright__)","copyright","Learn about program copyright"),
    
    ("author","print(__author__)","author","Learn about program developer name"),
 
    ("author","print(__author__)","author","Learn about program developer name"),
    
    ("feedback","color_print(f'If you have any questions or suggestions, please contact the developer as {__email__}','#00FFFF',html=True)","feedback","To get the way of feedback"),
    
    ("update", "update_program(_version_number)", "update", "To update the version"),
    
    ("license", "print(license())", "license", "To view the license"),
    
    ("email", "email()", "email", "Send emails to people"),
    
    ("bin","print(bin(int(command_data['Program']['bin']['run'])).replace('0b',''))","bin [number]","Convert an integer to binary number string"),
    
    ("hex","print(hex(int(command_data['Program']['hex']['run'])).replace('0x',''))","hex [number]","Convert an integer to hexadecimal number string"),
    
    ("oct","print(oct(int(command_data['Program']['oct']['run'])).replace('0o',''))","oct [number]","Convert an integer to octal number string"),
    
    ("ord","print(ord(command_data['Program']['ord']['run']))","ord [string]","Returns the integer representing its Unicode codepoint for a string representing a single Unicode character"),
    
    ("chr","print(chr(int(command_data['Program']['chr']['run'])))","chr [number]","Returns the string format of a character whose Unicode codepoint is the integer i"),
    
    ("md5","print(cipher(command_data['Program']['md5']['run']).en_md5)","md5 [text]","The text is encrypted using the md5 algorithm"),
    
    ("sha256","print(cipher(command_data['Program']['sha256']['run']).en_sha256)","sha256 [text]","Encrypt text with sha256 algorithm"),
    
    ("sha512","print(cipher(command_data['Program']['sha512']['run']).en_sha512)","sha512 [text]","Encrypt text with sha512 algorithm"),
    
    ("tf",{
            "-p": "two_factor._set_pin",
            "-a": "two_factor._add_factor",
            "-v": "two_factor._output",
            "-d": "two_factor._delete",
          },"tf -[p|a|v|d]",{
                              "-p": "To set the PIN code to protect the two-factor",
                              "-a": "To add the two-factor pin",
                              "-v": "To view the two-factor token",
                              "-d": "To delete the two-factor key"
                            }
    ),
    
    ("translate",{
                   "-y": "translate.YouDao().output(translate.YouDao().trans(' '.join(command_data['Program']['translate']['run']),langdet(' '.join(command_data['Program']['translate']['run']))[1]))",
                   "-g": "print(translate.Google().trans(command_data['Program']['translate']['run'],langdet(command_data['Program']['translate']['run'])[1]))"
                 },"translate [-(y|g) text]",{
                                                "-y":"To translate the word into Chinese/English by YouDao",
                                                "-g":"To translate the word into Chinese/English by Google",
                                             }
    ),

    ("download","download(command_data['Program']['download']['run'])","download [URL]","Download website resources")
    ]
    
    # Device
    Device = [
    ("name","print(device.name())","name","To get the device name"),
    
    ("type","print(device.type())","type","To get the device type"),
    
    ("bit", "print(device.bit())","bit","To get the device bit"),
    
    ("info","device.info()","info","To get the device info"),
    
    ("mac","print(device.Web().mac())","mac","To get the device mac"),
    
    ("fps","print(device.Fps().fps())","fps","To get the device fps"),
    
    ("network","print(device.Web().network())","network","To get the name of device network"),

    ("hostname","print(device.Web().hostname())","hostname","To get the device hostname"),
    
    ("timestamp","print(device.Time().timestamp())","timestamp","To get the device timestamp"),
    
    ("time","print(device.Time().time_local())","time","To get the local time"),
    
    ("ip",{
         "-l": "print(device.Web().IP().local())",
         "-p": "print(device.Web().IP().public())",
      },"ip -[l|p]",{
                       "-l":"To get the local ip address",
                       "-p":"To get the public ip address"
                    }
    ),
    
    ("system",{
                 "-n": "print(device.System().name())",
                 "-v": "print(device.System().version())",
                 "-l": "print(device.System().language())",
                 "-e": "print(device.System().encode())",
                 "-r": "print(device.System().release())"
      },"ip -[n|v|l|e|r]",{
                             "-n":"To get the system name",
                             "-v":"To get the system version",
                             "-l":"To get the system language",
                             "-e":"To get the system encode",
                             "-r":"To get the system release"
                          }
    ),
    
    ("processor",{
                    "-i": "print(device.Processor().info())",
                    "-c": "print(device.Processor().logic_count())",
      },"processor -[i|c]",{
                              "-i":"To get the local ip address",
                              "-c":"To get the public ip address"
                           }
    ),
    
    ("storage",{
                  "-t": "print(device.Storage().total(command_data['Device']['storage']['run']))",
                  "-u": "print(device.Storage().used(command_data['Device']['storage']['run']))",
                  "-f": "print(device.Storage().free(command_data['Device']['storage']['run']))",
                  "-p": "print(device.Storage().percent(command_data['Device']['storage']['run']))",
                  "-a": "print(device.Storage().available(command_data['Device']['storage']['run']))"
               },"storage [-(t|u|f|p|a) dir]",{
                                           "-t": "Used to get the total amount of storage",
                                           "-u": "Used to get the storage occupied",
                                           "-f": "Used to get the remaining amount of storage",
                                           "-p": "Used to get the percentage of storage occupied",
                                           "-a": "Used to get the memory available",
                                          
                                        }
    ),
    
    ("memony",{
                  "-t": "print(device.Memony().total())",
                  "-u": "print(device.Memony().used())",
                  "-f": "print(device.Memony().free())",
                  "-p": "print(device.Memony().percent())",
                  "-a": "print(device.Memony().available())"
               },"memony -[t|u|f|p|a]",{
                                           "-t": "Used to get the total amount of memony",
                                           "-u": "Used to get the memony occupied",
                                           "-f": "Used to get the remaining amount of memony",
                                           "-p": "Used to get the percentage of memony occupied",
                                           "-a": "Used to get the memory available"
                                          
                                        }
    ) 
    ]
    
    Calculate = [
    ("!","print(calculate.Expression().run(command_data['Calculate']['!']['run']))","! [expression]","Used by calculate"),
    
    ("dx",{
             "-d":"print(calculate.Function(command_data['Calculate']['dx']['run'][1]).derivative(command_data['Calculate']['dx']['run'][0]))"
          },"dx [level expression]",{
                                            "-d":"Used by differentiation"
                                         }
    ),
    
    ("triangle",{
                   "-a": "print(calculate.Triangle(float(command_data['Calculate']['triangle']['run'][0]),float(command_data['Calculate']['triangle']['run'][1]),float(command_data['Calculate']['triangle']['run'][2])).area)",
                   "-p": "print(calculate.Triangle(float(command_data['Calculate']['triangle']['run'][0]),float(command_data['Calculate']['triangle']['run'][1]),float(command_data['Calculate']['triangle']['run'][2])).perimeter)"},"triangle [-(a|p) a b c]",{
                                          "-a":"To calculate area", 
                                          "-p":"To calculate perimeter"
                                       }
    ),
    
    ("circle",{
                 "-a": "print(calculate.Circle(float(command_data['Calculate']['circle']['run'])).area)",
                 "-p": "print(calculate.Circle(float(command_data['Calculate']['circle']['run'])).perimeter)",
                 "-d": "print(calculate.Circle(float(command_data['Calculate']['circle']['run'])).diameter)",
              },"circle [-(a|p|d) radius]",{
                                              "-a":"To calculate area",                                                                                            "-p":"To calculate perimeter",
                                              "-d":"To calculate diameter"
                                           }
    )
    ]
    
    File = [
    ("workdir", "print(os.getcwd())", "workdir", "To get the work path"),
    
    ("home", "print(os.path.expanduser('•'))","workdir","To get the home path"),
    
    ("tree","tree(command_data['File']['tree']['run'])", "tree {dir}","Drawing the file tree directory"),
    
    ("view","filetool(command_data['File']['view']['run']).view","view {path}","To view the content of file"),
    
    ("info","filetool(command_data['File']['info']['run']).info","info {path}","To view the information of file"),
    
    ("scan","print(scanner(command_data['File']['scan']['run'][0],command_data['File']['scan']['run'][1]).scan_extension)","scan {path} {extension}","Scanning the path"),
    
    ("chdir","os.chdir(command_data['File']['chdir']['run'])\ntip_tick('The working directory is switched successfully')","chdir [path]","To switch the work path"),
    
    ("worklist","tree(os.getcwd())", "worklist", "To get the work dir list"),
    
    ("mkdir","os.mkdir(command_data['File']['mkdir']['run'])","mkdir [dir]","To create a dir"),
    
    ("edit","editingtool(command_data['File']['edit']['run']).edit","edit [filname]","Used to create a new text or edit the text"),
    
    ("bin",{
              "-r": "bin_system().restore",
              "-c": "bin_system().clear"
           },"bin -[r|c]",{
                             "-r":"To restore the file or the dir",
                             "-c":"To remove the file or the dir which in this bin"
                          }
    ),
    
    ("remove",{
                 "-c": "bin_system(path=command_data['File']['remove']['run']).common_remove",
                 "-s": "bin_system(path=command_data['File']['remove']['run']).super_remove",
                 "-d": "bin_system(path=command_data['File']['remove']['run']).direct_remove"
              },"remove [-(c|s|d) path]",{
                                            "-c":"To remove the file or the dir to the bin",
                                            "-s":"Use overwrite to remove the file or the dir directly and permanently",
                                            "-d":"To remove the file or the dir directly and permanently",
                                         }
)
    ]
    
    
    for name, code, operate, details in Key:
        _command_add("Key", name, code, operate, details)
    for name, code, operate, details in Global:
        _command_add("Global", name, code, operate, details)
    for name, code, operate, details in Program:
        _command_add("Program", name, code, operate, details)
    for name, code, operate, details in Device:
        _command_add("Device", name, code, operate, details)
    for name, code, operate, details in Calculate:
        _command_add("Calculate", name, code, operate, details)
    for name, code, operate, details in File:
        _command_add("File", name, code, operate, details)
    
def command_help(mode=None,command=None):
    if not mode and not command:
        for _mode in command_data:
            if _mode != 'Key':
                print('='*60)
            color_print(f'[{_mode}]','#00FF00')
            i = 0
            for _command in command_data[_mode]:
                i+=1
                color_print(f'{i}.{_command}','#00ABFF')
                text = [
                ('class:head','* Usage'),
                ('','\n'),
                ('class:body',f"• {command_data[_mode][_command]['help']['operate']}")
                ]
                style = {
                'head':'#FF00FF',
                }
                color_print(text,style,single=False)
                if type(command_data[_mode][_command]['help']['details']) == dict:
                    color_print('* Options','#5C5CFF')
                    for item in command_data[_mode][_command]['help']['details']:
                        print('•',item,command_data[_mode][_command]['help']['details'][item])
                else:
                    color_print('* Detail','#5C5CFF')
                    print('•',command_data[_mode][_command]['help']['details'])
                if i < len(command_data[_mode]):
                    print('-'*60)
    elif mode and not command:
        for _command in command_data[_mode]:
            i+=1
            color_print(f'{i}.{_command}','#00ABFF')
            text = [
            ('class:head','* Usage'),
            ('','\n'),
            ('class:body',f"• {command_data[_mode][_command]['help']['operate']}")
            ]
            style = {
            'head':'#FF00FF',
            }
            color_print(text,style,single=False)
            if type(command_data[_mode][_command]['help']['details']) == dict:
                color_print('* Options','#5C5CFF')
                for item in command_data[_mode][_command]['help']['details']:
                        print('•',item,command_data[_mode][_command]['help']['details'][item])
            else:
                color_print('* Detail','#5C5CFF')
                print('•',command_data[_mode][_command]['help']['details'])
            if i < len(command_data[_mode]):
                print('-'*60)
    else:
        if type(command_data[_mode][_command]['help']['details']) == dict:
            color_print('* Options','#5C5CFF')
            for item in command_data[_mode][_command]['help']['details']:
                print('•',item,command_data[_mode][_command]['help']['details'][item])
        else:
            color_print('* Detail','#5C5CFF')
            print('•',command_data[_mode][_command]['help']['details'])        


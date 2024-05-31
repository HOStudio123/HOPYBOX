print('''HOPYBOX %s Helps Documentation\n(HOPYBOX %s 帮助文档)\033[0m
  
\033[94mEdited in June 19, 2023\n(编辑于2023年月19日)\033[0m

\033[92mAll Chinese and English are translated by Google, and this program is written in UTF-8 encoding.\n(所有中英文均由谷歌翻译,并且本程序采用UTF-8编码编写)

This program supports Chinese and English.\n(这个程序支持中文与英文)

\033[93m[1]Command mode (指令模式)
Initiate this mode method:Enter the command 'take command'
(启动此模式方法:输入“take command”)\033[0m\033[95m
 ⎛ help {module/package} # Get helps of module
 ⎜ id {text} # Getting id of text
 ⎜ run {filename} # Running file of python
 ⎜ download {url} # Download web pages or files 
 ⎜ hoget {url} # Program url get 
 ⎜ bowget {url} # Initiate your browser and visit url 
 ⎜ qqname {qqnumber} # Get the name for the entered QQ 
 ⎜ qqhead {qqnumber} # Get the avatar of the input QQ 
 ⎜ email {email address} # Use Python to send mail, '{}' fill in the email address of the person you want to send to
 ⎜ install {package} # Install the latest package on PyPI
 ⎜ uninstall {package} # Uninstall package
 ⎜ del {filename} # Delete file or path
 ⎜ check version # Check program version
 ⎜ ipget {ip} # Look for the IPV4's address 
 ⎜ open {filename} # Open the file 
 ⎜ caculate {formula} # Even support absolute values and root calculations(√{x} and |{x}|) 
 ⎜ triangle {formula} # Trigonometric functions, Current supported recognition formats are sin, cos, tan, asin, acos and atan
 ⎜ pi # Return pi 
 ⎜ pkg list # List of installed packages
 ⎜ fps # Current equipment running speed 
 ⎜ translate {word} # YouDao translate 
 ⎜ timestamp # Timestamp 
 ⎜ time # Returns the current system time 
 ⎜ tree {filename} # Display the file information in the directory in the form of a tree (Example:tree /sdcard)
 ⎜ scan {pathname} {extension} # Look for specified suffix files in the specified path directory (Example:scan /sdcard .apk)
 ⎜ clear {pathname} {extension} # Clean up all object files in this path (Example:clear /sdcard .cache)
 ⎜ update {version} To get a update log about the version object (Example:update %s)
 ⎜ clear # Clear console 
 ⎝ exit # Exit 

\033[0m\033[93m[2]System mode (系统模式)
Initiate this mode method:Enter the command 'take system'
(启动此模式方法:输入“take system”)\033[0m\033[95m
 ⎛ {command} # Python terminal's command 
 ⎜ clear # Clear console 
 ⎝ exit # Exit 

\033[0m\033[93m[3]Python mode
Initiate this mode method:Enter the command 'take python'\033[0m\033[95m
 ⎛ debug {command} # Debugging simple python code
 ⎜ clear # Clear console 
 ⎜ interpreter # interpreter of python
 ⎜ python3 # interpreter of python
 ⎝ python # Interpreter of python

\033[0m\033[92m[4]Others (其它)
If you have any questions, please contact the developer as\033[1;93m hostudio.hopybox@foxmail.com \033[0m.\'\'' % (vcd,vcd,vcd)''')
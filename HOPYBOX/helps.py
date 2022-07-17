from .version import version_code as vcd
def helps_print():
  return '''\033[96mHOPYBOX %s Helps Documentation\n(HOPYBOX %s 帮助文档)\033[0m

\033[92mAll Chinese and English are translated by Google, and this program is written in UTF-8 encoding.\n(所有中英文均由谷歌翻译,并且本程序采用UTF-8编码编写)

This program supports Chinese and English.\n(这个程序支持中文与英文)

The parameters in '{}' are required, and the parameters in '[]' are optional.(“{}”中的参数是必需的，”[]”中的参数是可选的“)\033[0m

\033[93m[1]Command mode
Initiate this mode method:Enter the command 'take command'
(启动此模式方法:输入“take command”)\033[0m\033[95m
 ⎛ help {module/package} # Get module's helps 
 ⎜ id {text} # Get text's id 
 ⎜ run {filename} # Run python's file 
 ⎜ download {url} # Download web pages or files
 ⎜ hoget {url} # Program url get 
 ⎜ bowget {url} # Initiate your browser,and visit url 
 ⎜ qqname {qqnumber} # Get the name for the entered QQ 
 ⎜ qqhead {qqnumber} # Get the avatar of the input QQ 
 ⎜ email {mail} # Python send mail
 ⎜ install {package} # Install the latest package on PyPI
 ⎜ uninstall {package} # Uninstall package
 ⎜ del {filename} # Delete file or path
 ⎜ check version # Check program version
 ⎜ ipget {ip} # Look for the IPV4's address 
 ⎜ weather {city} # Get the weather for the entered city
 ⎜ open {filename} # Open the file 
 ⎜ caculate {formula} # Even support absolute values and root calculations(√{x} and |{x}|) 
 ⎜ triangle {formula} # Current recognition format:(sin/cos/tan/asin/acos/atan{x}) 
 ⎜ pi # Return pi 
 ⎜ pkg list # List of installed packages
 ⎜ fps # Current equipment running speed 
 ⎜ translate {word} # YouDao translate 
 ⎜ timestamp # Timestamp 
 ⎜ time # Returns the current system time 
 ⎜ path {filename} # Display file name and information in the directory
 ⎜ scan {pathname} {extension} # Look for specified suffix files in the specified path directory
 ⎜ clear {pathname} {extension} # Clean up all object files in this path
 ⎜ clear # Clear console 
 ⎝ exit # Exit 

\033[0m\033[93m[2]System mode
Initiate this mode method:Enter the command 'take system'
(启动此模式方法:输入“take system”)\033[0m\033[95m
 ⎛ [command] # Python terminal's command 
 ⎜ clear # Clear console 
 ⎝ exit # Exit 

\033[0m\033[93m[3]Python mode 
Initiate this mode method:Enter the command 'take python'
(启动此模式方法:输入“take python”)\033[0m\033[95m
 ⎛ debug [command] # Debugging simple python code
 ⎜ clear # Clear console 
 ⎜ interpreter # Python's interpreter 
 ⎜ ipython # IPython's interpreter 
 ⎝ python # Python's interpreter 

\033[0m\033[92mAt last
If you have any questions, please contact the developer as hostudio.hopybox@foxmail.com.''' % (vcd,vcd)
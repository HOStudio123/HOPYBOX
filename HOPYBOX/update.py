from .hopter import Error_pta
data_date = {
'0.0.1':'May 2, 2022',
'0.0.5':'May 2, 2022',
'0.1.0':'May 2, 2022',
'0.1.5':'May 2, 2022',
'0.9.6':'May 4, 2022',
'1.0.0':'May 6, 2022',
'1.2.0':'May 8, 2022',
'1.3.4':'May 15, 2022',
'1.4.7':'May 27, 2022',
'1.4.8':'May 28, 2022',
'1.4.9':'May 28, 2022',
'1.5.0':'May 28, 2022',
'1.5.1':'May 28, 2022',
'1.5.2':'May 28, 2022',
'1.5.3':'May 28, 2022',
'1.5.5':'May 28, 2022',
'1.5.6':'May 28, 2022',
'1.5.8':'May 30, 2022',
'1.6.0':'May 30, 2022',
'1.6.1':'May 30, 2022',
'1.6.3':'June 14, 2022',
'1.6.4':'June 14, 2022',
}

data_main = {
'0.0.1':'• This is the first version of HOPYBOX posted on PyPI, but not the first version of HOPYBOX, HOPYBOX\'s first version was born around January 28, 2022',
'0.0.5':'• Fixed some known issues',
'0.1.0':'• Fixed some known issues',
'0.1.5':'• Add some features to some instructions\n• Optimize details',
'0.2.0':'• Add some features to some instructions\n• Optimize details',
'0.2.1':'• Fixed some known issues',
'0.9.6':'• Updated program error\n• Added function to open files\n• Fixed some known issues',
'1.0.0':'• Fixed some known issues',
'1.2.0':'• Added calculator function\n• Fixed some known issues',
'1.3.4':'• Adjusted brightness of output text\n• Fixed some known issues',
'1.4.7':'• Update help document style\n• Fixed some known issues',
'1.4.8':'• Improve the help documentation\n• Added version display\n• Fixed some known issues',
'1.4.9':'• Fixed some known issues',
'1.5.0':'• Added program update log\n• Fixed some known issues',
'1.5.1':'• Fixed some known issues',
'1.5.2':'• Fixed some known issues',
'1.5.3':'• Fixed some known issues',
'1.5.5':'• Fixed some known issues',
'1.5.6':'• Updated README.md\n• Fixed some known issues',
'1.5.8':'• Updated README.md\n• Added Display Directory File Name and Information Command (path {filename})\n• Added scan file function(scan {pathname} {extension})\n• Fixed some known issues',
'1.6.0':'• Fixed some known issues',
'1.6.1':'• Fixed some known issues',
'1.6.3':'• Added clean file function(clear {pathname} {extension})\n• Fixed so many known issues',
'1.6.4':'• Fixed some known issues',
}

def look_for_data(version):
  try:
    print('\033[96mHOPYBOX {} Update Data\033[0m\033[92m ({})\033[0m\n\033[94m{}'.format(version,data_date[version],data_main[version]))
  except KeyError as e:
    Error_pta('KeyError','Command','No changelog found for this version','update '+version)
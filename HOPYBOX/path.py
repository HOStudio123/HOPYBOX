import os,time
def dirstree(startpath):
    path = startpath
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath,'').count(os.sep)
        indent = '│' * 1 * level + '╰─'
        print('%s%s' % (indent,os.path.split(root)[1]))
        for i in files:
          print(indent+i)
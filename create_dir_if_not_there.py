import os #import the os module
MESSAGE = 'The directory already exists'
TESTDIR = 'testdir'

try:
    home = os.path.expanduser("~") #expand "~"or"~user" if
    print(home) #print the location
    if not os.path.exists(os.path.join(home,TESTDIR)):
        os.makedirs(os.path.join(home,TESTDIR))
    else:
        print(MESSAGE)
except Exception as e:
    print(e)


"""
1.cd - 返回上一目录
2.os.makedirs创建目录
  os.path.join("str1","str2")
  os.path.exists("path1")
  os.path.expanduser('~'|"~username") #"/root"

"""

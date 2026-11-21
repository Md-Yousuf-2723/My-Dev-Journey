# Modules are pre written code of other developers
# that can be imported by python script 
import os # os : Operating Sysem --> a module name of python
# that comes inbuilt in python
os.getcwd() # getcwd --> cwd : current work directory
# getcwd() is a funtion written in os module

import sys # Sys is inbuilt module that comes with py
sys.platform # platfrom is variable in sys module which
# holds the platfrom name I am working currently

from importlib import reload # importlib is a collection 
# of library, from the importlib I have imported reload
reload(hello_python) # reload used to reload a module if 
# any change is made

import math # Give access to mathmatical tools
print(math.pi)
import random
random.random() # Generates random numbers
random.choice([1,2,3,4,5]) # randomly chooses any 
# number from the list I have given to it

username = "Yousuf"
print(dir(username)) # dir tells what functionalities 
# the obj type has. Like here username is string type. So it 
# will tell what functionalities 
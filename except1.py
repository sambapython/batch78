print("main block")
from time import sleep
try:
    print("try")
    sleep(20)
except Exception as err:# this generic block catched by all python program level exceptions
    print("Exception")
except:# this will be catached for program and system level exceptions.
    print("except")
print("End main block")

# write a program keep program 20 minutes sleep, add some file data in except blocks and check which 
# except block is going to catch while restarting the machine.
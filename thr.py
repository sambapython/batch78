import threading
import time
def fun1():
	time.sleep(3)
	print("fun1 done")
def fun2():
	time.sleep(3)
	print("fun2 done")
t1=time.time()
thr1 = threading.Thread(target=fun1)
thr2 = threading.Thread(target=fun2)
thr1.start()
thr2.start()
t2=time.time()
print(t2-t1)
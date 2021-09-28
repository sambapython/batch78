a=100
b=2000
import pdb;pdb.set_trace()
print(f"a={a}, b={b}")
res=a-b
print("result=",res)
def fun(x,y):
    print(f"x={x}, y={y}")
    res=x+y
    print("result=",res)
print("hello")
for i in range(-4,4):
    if i!=0:
        print(10/i)
fun(10,20)
print("done")
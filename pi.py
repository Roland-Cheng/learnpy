import random
import time
NUM=eval(input("请输入计算次数：\n"))
t = time.perf_counter()
hit = 0
for i in range(NUM):
    x,y=random.random(),random.random()
    if x**2+y**2<=1:
        hit+=1
pi=4*hit/NUM
print("圆周率是：{}".format(pi))
print("运算时间是：{:.6f}s".format(time.perf_counter()-t))
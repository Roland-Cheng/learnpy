TempStr = input("请输入温度：")
if TempStr[-1] in ['F', 'f']:
    c = (eval(TempStr[0:-1]) - 32)/1.8
    print("转化后的温度是{:.2f}C".format(c))
elif TempStr[-1] in ['C', 'c']:
    f = 1.8*eval(TempStr[0:-1])+32
    print("转化后的温度是{:.2f}F".format(f))
else:
    print("输入格式错误")

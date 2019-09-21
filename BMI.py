height,weight = eval(input("请输入身高、体重【使用逗号分隔】\n"))
if height > 100:
    bmi = weight/pow(height/100,2)
else:
    bmi = weight/pow(height,2)
if bmi <18.5:
    a = "偏瘦"
elif bmi<24:
    a = "正常"
elif bmi<28:
    a="偏胖"
else:
    a="肥胖"
print("您的BMI值是：{:.2f}您的身体状况是：{}".format(bmi,a))
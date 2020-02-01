x=0.2
y=1/239
arctanx=0
arctany=0
for i in range(0,10):
    arctanx=arctanx+pow(x,2*i+1)*pow(-1,i)/(2*i+1)
    arctany=arctany+pow(y,2*i+1)*pow(-1,i)/(2*i+1)
pi=4*(4*arctanx-arctany)
print(pi)

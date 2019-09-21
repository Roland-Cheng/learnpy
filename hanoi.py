count = 1
def hanoi(n,start,end,mid):
    global count
    if n==1:
        count +=1
        print("{}:{}->{}".format(1,start,end))
    else:
        count+=1 
        hanoi(n-1,start,mid,end)
        print("{}:{}->{}".format(n,start,end))
        hanoi(n-1,mid,end,start) 
hanoi(5,"a","b","c")
print(count)    

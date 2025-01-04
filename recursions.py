def fibonacci(a,b,count):
    c=[] #to store fibonacci number
    for i in range(count):
        c.append(a) #adding each new value of a in c
        a,b=b,a+b 
    return c
    

a=0
b=1
length=10
result=fibonacci(a,b,length)
print(result)



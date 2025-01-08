def sum():
    x=2
    return x+2

y=sum()
print(y)

#now this function is equivalent to lambda function for writing in short syntax

sum=lambda x=2:x+2 #here sum is the nam of function, x=2 is the initialized argument and x+2 is the return value
cube=lambda x=3:x*x*x
avg=lambda x,y,z:(x+y+z)/3
y=sum(),cube()  #function can be called at once in a single variable where the values will be stored in tuple which are immutable
print(y)
print(int(avg(2,2,2)))


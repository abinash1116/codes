def cube(x):
    return x*x*x
l=[1,2,3,4]
m=[]
for i in l:
    m.append(cube(i))  #this sppend is used to add cube values in new list that is in m we are not changing the value of list l
print(m)
print(l)


#MAP FUNCTION
def sq(x):
    return x*x
n=[1,2,3,4]
newn=list(map(sq,n)) #here all the elements are typecasted to list and map directly squares each elements in the sequence
print(newn)

#using lambda function for same function

n=[1,2,3,4]
sq=list(map(lambda x:x*x,n))
print(sq)

#FUILTER FUNCTION

n=[2,3,4,5,1,0]
greater=list(filter(lambda x:x>2,n)) #this will only print that values which is greater then 2
print(greater)

# simplified function without using lambda function

def greater(x):
    return x>2
n=[1,2,3,4]
great=list(filter(greater,n))
print(great)

#REDUCE FUNCTION

from functools import reduce

n=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,n) #this will simply add all the elements n a sequence manner i.e., first 1+2=3,3+3=6,6+4=10,10+5=15 and hence gives the final reduce answer as 15
print(sum)

# simplified function without using lambda function

def add(x,y):
    return x+y

n=[1,2,3,4,5]
sum=reduce(add,n) #here add which is function name is taken as the argument for function sum so we can say that map,filter and reduce are higher-order function
print(sum)
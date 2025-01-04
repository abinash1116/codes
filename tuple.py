x=(1,2,3)
print(type(x))
print(x)

x=("abinash",) #if you are writing one elements and creating the tuple then it is compulsory that you have to place , after that one element otherwise the element is taken as other data types value
print(type(x))
print(x)

x=(1,2,3)
if 2 in x:
    print(x)

#other examples are similar to list data type but the elements cannot be changed like in the list

x=[1,2,3,4]
y=list(x) #converting tuple to list
y.append(5) #adding new elements to the list
y.pop(3) #pop removes the following elements of the index assigned in the paranthesis of pop()
y[2]=6 #adding 6 in the index 2
x=tuple(y) #converting list to tuple
print(x)


x=[1,2,3,4]
y=[5,6,7,8]
z=x+y
print(z)

a=[2,2,3,4,2]
print("the number of 2 is",a.count(2)) #it counts the number of elements present in the tuple

x=(1,2,3)
print(x.index(2)) #it helps to find the index of the given element in tuple 

x=(1,2,3,4,5,4,3,2,1,1,2)
print(x.index(1,4,10)) #here (element,start of slicing,end of slicing) this is the syntax of given index method

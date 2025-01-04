marks=[100,90,80,70,60,"abinash"]
print(marks)

print(marks[1])
print(marks[-4]) #this means total length of the elements in list - 4, i.e., it gives 5-4=1

if 90 in marks:
    print("is present")
else:
    print("not present") #this helps to find if the given character is present in the given list or not


if "sh" in "abinash": #this helps to print if the given character is present in the following string of the list or not
    print("yes")

print(marks[1:5:2])  #2 oota ko gap didai answer nikalxa from index 1 to 5

lst=[i for i in range(4)]
print(lst)
print(type(lst))

name=["abinash","oli","ram"]
name1=[item for item in name if "a" in item] #list comprehensions
print(name1)


x=[1,2,3,4,5]
x.append(6) #helps to add 6 in the list
print(x)

x=[4,2,1,3,5]
x.sort() #helps to arrange the list in ascending order
print(x)

x=[2,3,1,5,6,4]
x.sort(reverse=True) #helps to print in descending order
print(x)

x=[5,2,1,4,6]
x.reverse() #helps to reverse the original elements of the list
print(x)

x=[1,2,3,4,5] #if there are two same elements in the list then the index is assigned to the first occuring character
print(x.index(3)) #helps to give the index or position of the assigned or given value
print(x) 

x=[1,2,3,4,5,1]
print(x.count(1)) #it helps to count how many times the characters have occured ein the following list
print(x)

x=[1,2,3,4,5,1]
m=x.copy()  #this will copy the same elements of the x and make another list of name m 
m[0]=0  #here the first element of the list is replaced by 0 is I print m but if i print x then I will get all the elements of the list x
print(m)

x=[1,2,3,4]
x.insert(4,5) #helps to insert the new element to the list to the given index i.e., 5 is added to the position 4
print(x)

x=[1,2,3,4]
y=[5,6,7,8]
x.extend(y) #it adds the elements of y at the end of the list x
print(x)

x=[1,2,3,4]
y=[5,6,7,8]
z=x+y #it helps to merge two list and display in a single list and it displays the value according to the order of list assigned i.e., it displays the value of x first if z=x+y while it displays the value of y first if z=y+x
print(z)


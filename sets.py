a={"abinash",8,4,3,2}
print(a)

abinash=set() #creating empty set
print(type(abinash))

for i in a:
    print(i)

a={2,3,4}
b={5,6,7,2,3}
print(a.union(b)) #helps to print union of a and b
print(a | b) #this is another method to find union


a.update(b)  #helps to update or add elements of b in set a
print(a)

a={2,3,4}
b={5,6,7,2,3}
c=a.intersection(b)  #helps to print the intersection between a and b
print(c)
print(a.intersection(b)) #it also helps to find the intersection 
print(a&b) #this is another method to find the intersection between a and b 

a.intersection_update(b)  #helps to update the intersection of b in set a
print(a)


d=a.symmetric_difference(b) #helps to print the elements that are not common in both of the sets i.e., except intersection
print(d)

a.symmetric_difference_update(b) #helps to update the symmetric_difference of b in set a
print(a)

a={2,3,4}
b={5,6,7,2,3}
e=b.difference(a)  #helps to print only the original set not in both sets
print(e)

b.difference_update(a)   #helps to update the difference of a in set b
print(b)   

a={2,3,4}
b={5,6,7}
f=a.isdisjoint(b)  #helps to check whether their are common items in sets or not,returns false if there is common else return true
print(f)

a={2,3,4}
b={2,3,5}
c=a.issuperset(b)  #checks whether all the elements of b are in a or not if all elements are present then it returns true else returns false
print(c)
d=b.issubset(a)  #checks if b is the subset of a or not.i.e., if all the elements of b are present in a or not
print(d)

a={2,3,4}
a.add(5) #helps to add new elements to the set
print(a)

a={2,3,4}
b={5,6,7}
a.update(b)  #adds elements of b in a
print(a)

a={2,3,4}
a.remove(2)  #remove specified element from set
print(a)

a={1,2,3}
b=a.pop() #it removes any value from set and gives which value is removed
print(a)
print(b)

# c={2,3,4}
# del c
# print(c)  #this throws an error since we have deleted set c and c is not defined further 

a={2,3,4}
a.clear( ) #clears only the items from the set
print(a)

a={2,3,4,5,6,6}
if 5 in a:
    print("is present") #checks if the item is present in the set or not
else:
    print("not present")

# a={2,3,4}
# a.update({5})
# print(a)
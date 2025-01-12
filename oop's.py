# class and objects

class person:
    def __init__(self,name="",age=None,gender=""):  #constructor,passing an arguments and we have to assign some value either None or blank string else it will give argumenterror
        self.name=name  #here self acts as a instance which is changed when a new instance is formed 
        self.age=age #here self is changed according to the instance,(.name) is the instance variable and (=age) here the values are stored
        self.gender=gender

    def __str__(self): #calling the self and string representation and assigning the value of each object
        return f'Name: {self.name} , Age:{self.age} , Gender:{self.gender}\n'

    

a=person() #here a is instance and a=person() is object
a.name="Abinash" #this is a object where (a) is instance, (.name) is instance variable and ("Abinash") is the value assigned to instance variable
a.age=19
a.gender="Male"
print(a)


b=person() #here b is instance and b=person() is object         

b.name="Ram"
b.age=20
b.gender="Male"
print(b)

c=person() #here c is instance and c=person() is object
c.name="Sita"
c.age=21
c.gender="Female"
print(c)


# decrator

def greet(f): #decorator function which helps to modifiy the specific function
    def info():
        print("WELCOME EVERYONE!!")
        f()
        print("THANKS FOR VISITING")
    return info

def inside():
    print("YOU ALL ARE AWESOME")

greet(inside)() #you can individally give decorator to specific function like this 


# def greet(f): #decorator function which helps to modifiy the specific function
#     def info():
#         print("WELCOME EVERYONE!!")
#         f()
#         print("THANKS FOR VISITING")
#     return info

# @greet #you can also directly use the decorator syntax over here
# def inside():
#     print("YOU ALL ARE AWESOME")


# inside() 


#inheritance


class employee:
    def __init__(self,name="",ids=None):
        self.name=name 
        self.id=ids
    
    def info(self):
        print(f"the name is employee {self.id} is {self.name}")


class employees(employee): #this is inheritance where I made a new class named employees and kept previous class as argument 
    def infos(self):
        print("this is the inheritance class")


a=employees() #here I need to class new class i.e., child class to show the information written in new class
a.name="Abinash"
a.id=12
a.info()
a.infos()

empl=[] #creating empty list to store the name and id of employees
lists=["Rabi","Hari","Ram","Shaym"]
ids=[13,14,15,16]
for i in range(4):  
    emp=employees(lists[i],ids[i])
    empl.append(emp)  

for emp in empl:
    emp.info()
    emp.infos()


#Access and Modifiers

class name:
    def __init__(self,name=""):
        self.name=name  #this is public access which is by default access in python

    def public(self):
        print(f"{self.name} is public value")
a=name()
a.name="abinash"
a.public()



class name1:
    def __init__(self):
        self.__name="Abinash" #this is private access

a=name1()
# print(a.__name)  #this cannot be accessed since this is private access 
print(a._name1__name) #This is the correct method of accessing the private access (instance._classname__argument)
print(a.__dir__()) #since dir is method so we have to call it using paranthesis


class name2:
    def __init__(self):
        self._name="Abinash" #this is inidcation of protected access

a=name2()
print(a._name) #this is the method of accessing protected access method
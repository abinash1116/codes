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



class books:
    kitab="science"  #class variable

    def pustak(self):
        print(f"The name of book is {self.name} and the kitab is {self.kitab} ") #instance variables
    
    @classmethod   #this will change the class varaiable  i.e., it will change the first argument as class here self is changed to books.kitab but in instance it would be changed as bidyarthi.kitab
    def newpustak(self,kitab1):
        self.kitab=kitab1


bidyarthi=books()
bidyarthi.name="Hero"
bidyarthi.pustak()
bidyarthi.newpustak("Management")
bidyarthi.pustak()
print(books.kitab)


#class method as alternative constructor

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def changestr(cls,string):
        return cls(string.split(" ")[0],int(string.split(" ")[1]))  #this is the alternative class constructor


person2=person("hari",19)
print(person2.name)
print(person2.age)
string="Abinash 19"
person1=person.changestr(string) #now this will convert my whole string value to individual instance variable by seperating the values
print(person1.name)
print(person1.age)


class person:
    age=20
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def returnvalue(self):
        print(f"The name of persons of age {self.age} is {self.name} and the salary of person is {self.salary}")

    @classmethod

    def changes(cls,newage):
        cls.age=newage

    @classmethod
    def classconstructor(cls,constructor):
        _,name,salary=constructor.split(" ")
        return cls(name,int(salary))
    
person1=person.changes(19)
person1=person("Abinash",200000) 
person1.returnvalue()
# person2=person.changes(21)
constructor="21 Ram 40000"
person2=person.classconstructor(constructor)
person2.returnvalue()
# print(help(person))   #this will help to know all the methods,variables used in the class person


#super keyword

class parent:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        print("this is parent class")

    def parent_method(self): #if this self argument is not given then it will raise noargument error
        print("for the use of super keyword")
    
    def parent2_method():
        print("this should not be printed")

class child(parent): #this is the child classs which will inherit all the methods and all the functions that are used in parent class
    def child_method(self):
        print("this is child class")
        super().parent_method() #this code is only accessable when we include parent class name in the argument of child class 
    def __init__(self, name, id,age):
        super().__init__(name, id)
        self.age=age

childcall=child("Abinash",100,19)
childcall.child_method()
print(childcall.name)
print(childcall.id)
print(childcall.age)


#operator overloading
class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}"
        
    def __add__(self,x):
        return vector(self.i+x.i,self.j+x.j,self.k+x.k) #here python will create a tuple and the values are seperated using comma(,)
    

a=vector(1,2,3)
print(a)
b=vector(2,3,4)
print(b)
c=vector(3,4,5)
print(c)

print(a+b+c)



#types of inheritance

#1) single inheritance

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

class snake(Animal):
    def __init__(self, name, species,sound):
        self.sound=sound
        super().__init__(name, species)


python=snake("Snake","Python","SSSSSSHHHHH")
print(python)
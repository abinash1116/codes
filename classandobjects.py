class person:
    def __init__(self,name,age,gender):  #constructor,passing an arguments 
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
print(a)


# decrator

def greet(f): #here f is just an arguments
    def mf(): #here mf refers to the modified argument
        print("WELCOME")
        f()
        print("THANK YOU SO MUCH")
        return mf
    
@greet #here greet is the decorator which has modified the function (a)
def ab():
    print("I hope you are doing great")

ab()   
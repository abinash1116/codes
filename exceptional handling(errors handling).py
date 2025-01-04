try:
    a=int(input("enter any value:"))
    # print(a)
    num=[2,5]
    print(num[a])
except ValueError:
    print("enter the correct integer") #returns if value is not given correctly 
except IndexError:
    print("index error") #returns if the index is given incorrect



#finally handling(keyword)
def fun():
    try:
        a=[1,2,3]
        i=int(input("enter the value of a:"))
        print(a[i])
        return 0
    except:
        print("error!!")
        return 1
    finally:
        print("Hello there") #this is always executed,either program produces error or the program doesn't

x=fun()  #here the returning value is printed i.e., either 0 or 1
print(x)

# we could have directly written the print statement without even using finally code but if we write the code in some def function then it will not return print statement if finally keyword is not used.
def fun():
    try:
        a=[1,2,3]
        i=int(input("enter the value of a:"))
        print(a[i])
        return 0
    except:
        print("error!!")
        return 1
print("Hello there") #this is not executed since finally code is not used but if we haven't used def function and directly written print statement then this would work 

x=fun()  #here the returning value is printed i.e., either 0 or 1
print(x)

# raising an error
a=int(input("enter any value between 4 and 10:"))
if(a<4 or a>10):
    raise ValueError("error occured")

a=input("enter any string:")
if(a!="quit"):
    raise ValueError("it is not quit")
else:
    print("well done")
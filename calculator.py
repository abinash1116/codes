# WAP to create a calculator which can perform all the operations
# a=5
# b=5
# sum=a+b
# print("the sum of a and b is",sum)
# product=a*b
# print("the product of a and b is",product)
# subtraction=a-b
# print("the subtraction of a and b is",subtraction)
# division=a/b
# print("the division of a and b is",division)
# exponential=a**b
# print("the exponential of a and b is",exponential)#a ko power nikaleko i.e a^b=a**b
# modulus=a%b
# print("the modulus of a and b is",modulus)
# floor_division=a//b
# print("the floor_division of a and b is",floor_division)


# print("**\t%\t//\t\n7\t8\t9\t+\n6\t5\t4\t-\n3\t2\t1\t*\n.\t0\t=\n")
# a=float(input("enter the value: "))
# b=float(input("enter the value: "))
# c=input("operators(+,-,*,/,//,**,%): ")
# if c == "+":
#     print(f"the sum of {a} and {b} is {a+b}")
# elif c == "-":
#     print(f"the difference of {a} and {b} is {a-b}")
# elif c == "*":
#     print(f"the product of {a} and {b} is {a*b}")
# elif c == "/":
#     print(f"the division of {a} and {b} is {a/b}")
# elif c == "//":
#     print(f"the floor_division of {a} and {b} is {a//b}")
# elif c == "**":
#     print(f"the expontential of {a} and {b} is {a**b}")
# elif c =="%" :
#     print(f"the modulus of {a} and {b} is {a%b}")
# else :
#     print("enter the correct operator")

# the above code is also correct second code is just a try to create and make output look like a calculator

print("**\t%\t//\t\n7\t8\t9\t+\n6\t5\t4\t-\n3\t2\t1\t*\n.\t0\t=\t/\n")
def calc(number):
    value=input(number)
    if value.isnumeric(): 
        return int(value)
    else:
        return float(value)

a=calc("enter the value:")
b=calc("enter the value:")
c=input("operators(*,+,/,//,%,**,-):")
if c  == "+":
    result=a+b
elif c == "*":
    result=a*b
elif c == "-":
    result=a-b
elif c == "/":
    if b != 0:
        result=a/b
    else:
        result="maths error"
elif c == "//":
    if b != 0:
        result=a//b
    else:
        result="maths error"
elif c == "**":
    result=a**b
elif c == "%":
    if b != 0:
        result=a%b
    else:
        result="maths error"
else:
    result="enter the correct input"
print(result)






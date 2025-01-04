a=int(input("enter the age :"))
print(a)
if a >= 15:
    print("you are eligible")
elif a <=10:
    print("you are below age")
else:
    print("you are not eligible")


# time program

import time
timestamp=time.strftime('%H:%M:%S') #strf function is used to define the time in the program
print(timestamp)
if(timestamp <= "11:59:59"):
    print("GOOD MORNING")
elif(timestamp <= "5:59:59"):
    print("GOOD AFTERNOON")
else:
    print("GOOD EVENING")
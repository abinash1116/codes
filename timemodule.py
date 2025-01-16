import time
def whileloop():
    i=0
    while i<10:
        i=i+1
        print(i)

def forloop():
    for i in range(1,11):
        print(i)

init=time.time()  #the initial time of the loop before execution is saved to init 
forloop()
t1=time.time()-init #subtracting the present time with initial time which gives the executuon time required by the code to execute
init=time.time() #setting new initial time for while loopS
whileloop()
t2=time.time()-init 
print(t1) #this prints the execution time of for loop and it is printed in second
print(t2)  #this prints the execution time of while loop

def sleep():
    a=4
    time.sleep(3) #this helps to delay the code execution here 3 is given which means that after 3 second the code will be executed and 4 will be printed
    print(a)

init=time.time()
sleep()
t=time.time()-init
print(t)

t=time.localtime()  #this helps to give the local time of my place or where the code is being runned
new_time=time.strftime("%y-%m-%d %H:%M:%S",t) #gives the time value as a string based on a specified format in a human readable form
print(new_time)
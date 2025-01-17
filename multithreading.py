import threading
import time

def fun(seconds):
    print(f"The time taking to run the code is {seconds} seconds")
    time.sleep(seconds)

time1=time.perf_counter() #perf_counter()method helps to evaluate the time 
t1=threading.Thread(target=fun, args=[3])
t2=threading.Thread(target=fun, args=[2])
t3=threading.Thread(target=fun, args=[1])

t1.start() #this will help to start the code at a time and display the code without letting one to complete 
t2.start()
t3.start()

t1.join() #now this will start the code at once but wait for all the function to run and complete the execution before displaying
t2.join()
t3.join()

time2=time.perf_counter()  #calculating time
print(time2-time1)

for i in range(12):
    if i== 11:
        break  #breaks the loop function and completes the program
    print("5 x" , i , "=" ,5*i)


for i in range(12):
    if i== 11:
        continue  #breaks the given condition in loop function and continues the remaining program i.e., breaks only the iteration  
    print("5 x" , i , "=" ,5*i)

for i in [2,3,4,5,6,7,8,9,10]:
    if (i%2!=0):
        continue
    print(i,"\n")

for i in [2,3,4,5,6,7,8,9,10]:
    if (i%2!=0):
        break
    print(i)
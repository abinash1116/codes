#for-loops
name="abinash"
for i in name:
    print(i)
    if (i=="b"):
        print("b is special letter") #b paxadi yo string haldinxa

colors=["red","blue","green","black"]
for i in colors: #here i stores thhe indiiviual elements of the list and print it individually
    print(i)
    for l in "red":
        print(l)


for i in range(5):
    print(i) #it prints the number from 0 to 4
    print(i+1) #ir prints the number from 1 to 5

for i in range(1 , 6): #it prints the number from 1 to 5
    print(i)

for i in range(1, 15 , 2): #it prints the number from 1 to 15 but with the gap interval of 2 i.e., 1,3,5,7,.....,etc.
    print(i)

#using else with for loop
for i in range(5):
    print(i)

else:
    print("please reuse the loop")

for i in range(5):
    print(i)
    if i == 4:
        break  

else:
    print("please reuse the loop") #else statement is not executed if if statement is break or loop is break


# while loops

i=0
while(i<=20):
      i=int(input("enter the number "))
      print(i)
      if(i>20):
          print("return back!!!!")

i=0
while i< 5:
    print(i)
    i=i+1
    if i ==4:
        break

else:
    print("please reuse the loop")  #else statement is not executed if if statement is break or loop is break


    

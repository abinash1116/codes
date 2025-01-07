marks=[99,98,5,6]
for index,mark in enumerate(marks): #enumerate automatically increments the index value i.e., from 0 to ,......
    print(mark)
    if(index == 3):
        print("poor")

marks=[99,98,5,6]
for index,mark in enumerate(marks,start=1): #if you want to start your loop from any certain index then you can specify the index using start 
    print(mark)
    if(index == 3):
        print("poor")
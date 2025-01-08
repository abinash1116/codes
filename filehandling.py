# f=open('myfile.txt','r')
# text=f.read() #this will only read the texts that are written in myfile.txt 
# print(text)
# f.close()

# # f=open('myfile.txt2','w')
# # text="hey man how are you??"
# # f.write(text) #this will eventually write the text in myfile.txt2 it self and if the file is not created then it will automatically create the file
# # print(text) 
# #f.close()

# # with open('myfile.txt2','w') as f: #this will automatically close the file and we don't even have to write f.close() to close the file
# #   text="hey man how are you??"
# #   f.write(text) 
# #   print(text) 


# f=open('myfile.txt2','a') #this will append or add extra text in your file or it will also automatically append the file if the file doesnot exist
# text="hey man how are you??\n all good?"
# f.write(text) 
# print(text) 

# # with open('myfile.txt','x') as f: #throws an error since myfile.txt already exist
# #     text="hello everyone"
# #     f.write(text)
# #     print(text)


# # with open('myfile0.txt','x') as f: #this will create a new file named myfile1.txt
# #     text="hello everyone"
# #     f.write(text)
# #     print(text)


# with open('myfile0.png','wb') as f:  #this will read the image i.e., binary iumage that is in the myfile0.png
#     file=b"this is a perfect image"
#     f.write(file)
#     print(file)

# # Step 1: Write binary data to a file
# with open('example.bin', 'wb') as f:
#     binary_data = b'\x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64'  # Binary data for "Hello World"
#     f.write(binary_data)

# # Step 2: Read the binary data back from the file
# with open('example.bin', 'rb') as f:
#     read_data = f.read()
#     print("Binary Data in the File:", read_data)  # Display the binary data
#     print("Decoded Text:", read_data.decode('utf-8'))  # Decode to text (if possible)


with open('myfile.txt','r') as f:  #this will read all the lines seperetely
    i=0
    while True: # A while True loop is used to read lines from the file until the break statement is encountered.
        i=i+1
        line=f.readline().strip() # Strip removes leading/trailing whitespace, including newlines
        if not line:  #if there is no text written in myfile.txt then it will break the loop
            break
        m1=line.split(",")[0]  #the numbers that are written in myfile.txt are in string for eg("56,54,63") so split(",") are used to split that numbers seperately. [0],[1],[2] this is the process of giving index number i.e., now m1 is set to 55 as 56 is in index 0 
        m2=line.split(",")[1] #since every lines are read seperately 3 lines of numbers are printed seperetely
        m3=line.split(",")[2]
        print(f"the marks of {i} in maths is {m1}")
        print(f"the marks of {i} in science is {m2}")
        print(f"the marks of {i} in computer is {m3}")
        print(line)


# with open('myfile.txt','w') as f:   #this will write the lines in myfile.txt replacing previous data
#     lines=["line1","line2","line3"]
#     for line in lines:
#         f.write(line+'\n')


with open('myfile.txt','a') as f:   #this will append the lines in myfile.txt 
    lines=["line1","line2","line3"]
    for line in lines:
        f.write(line+'\n')

with open('seek.txt','r') as f:
    f.seek(10) #this will simply skip before bytes of character i.e., from 0-9 and starts reading from 10th character
    data=f.read(6) #this will only print the next 6 bytes of character from 10th bytes
    print(data)


with open('seek.txt','r') as f:
    f.read(12) #this will read first 12 bytes of characters
    position=f.tell() #this will tell the current position that we are working 
    print(position)


with open('newfile.txt','w') as f:
    f.write("hello world")
    f.truncate(7) #this will allocated the given spaces in newfile.txt or we can simply say that only 7 bytes of character are printerd  

with open('newfile.txt','r') as f: #this code is written to print the expected output
    a=f.read()
    print(a)
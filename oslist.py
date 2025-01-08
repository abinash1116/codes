import os

folder=os.listdir("files")

for folders in folder:
    print(folders)  #this will list all the subdirectory that are present in the files
    print(os.listdir(f"files/{folders}"))  #this will print all the folders that are inside sub directories(book)

cmd="date"

os.system(cmd) #this will show todays date
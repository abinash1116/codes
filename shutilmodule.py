import shutil
import os
shutil.copy("shutilmodule.py","copy.py") #this will create a new copy.py file and copy all the codes or text written in this file
# shutil.copytree("newfolder","files.txt") #this will create a new folder and copy all the files and written codes or text to new folder(files.txt),first you have to create a folder named (newfolder) 
# shutil.move("newfolder/try.file","try.file") #this will remove the (try.file) from newfolder and move outside the folder creating independent file
# shutil.rmtree("files.txt") #removes the folder
os.remove("newfolder/try.file") #removes the file from the folder
os.remove("try.file") #removes the idependent file

# I made a new folder named dummy folder in thispc where I have coded a program which can print folders with files as much as I can using loop
import os

if(not os.path.exists("files")):
    os.mkdir("files")

if(not os.path.exists("files")):
    for i in range(0,100):
        os.mkdir(f"files/folders{i*1}")  #this will create other 99 folders inside file

#code for renaming the files is in rename.py folder
#code for oslist is in oslist.py
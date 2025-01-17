import shutil
import os
shutil.copy("shutilmodule.py","copy.py") #this will create a new copy.py file and copy all the codes or text written in this file
# shutil.copytree("newfolder","files.txt") #this will crewte a new folder and copy all the files and written codes or text to new folder(files.txt)
# shutil.move("newfolder/try.file","try.file") #this will remove the (try.file) from newfolder and move outside the folder creating independent file
# shutil.rmtree("files.txt") #removes the folder
os.remove("newfolder/try.file") #removes the file
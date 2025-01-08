import os

for i in range(0,100):
    source=f"files/books {i}"
    destination=f"files/books{i}"
    if(os.path.exists(source)):
        os.rename(source,destination)  #this will rename all the files that are created previously

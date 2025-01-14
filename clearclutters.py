import os

if(not os.path.exists('clutters')):  #This will create a file named clutters if not exists
    os.mkdir('clutters')

if(not os.path.exists('clutters')):
 for i in range(0,10):               #creating 10 more files inside clutter folder
    os.mkdir(f"clutters/clutter{i+1}")

for i in range(0,11):
    source=f'clutters/{i+1}.png{i+1}'
    destination=f'clutters/{i+1}.png'   
    os.rename(source,destination)     #renaming the files inside clutters
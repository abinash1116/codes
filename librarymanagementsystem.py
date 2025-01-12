class library:
    def __init__(self,books,No):
        self.books=books
        self.nos=No
    
    def lib(self):
        print(f"The number of books in library is {self.nos} and the books are {self.books} ")


l=[]
book=["Maths","IIT","DigitalLogics","C-programming","Physics"]
number=[1,2,3,4,5]
book.append("Chemistry")
number.append(6)
if(len(book) != len(number)):
    raise ValueError
for b in range(len(book)):
    libr=library(book[b],number[b])
    l.append(libr)
    

for libr in l:
    libr.lib()




        
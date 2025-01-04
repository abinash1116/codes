a=int(input("enter the value of a:"))
match a:
    case 0:
        print("a is zero")
    case 4:
        print("a is four")
    case 2:
        print("a is two")
    case _ if a!=20:   #case _ refers to defualt case
        print(a," is not 20")
    case _ if a!= 30:
        print(a,"is not 30")
    case _:
        print(a)
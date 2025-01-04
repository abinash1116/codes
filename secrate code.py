a=input("if you want to code or decode??")
print(a)
#for coding
def code():
    b=input("enter the word:")
    if(len(b)>=3):
        c=b[1:]+b[0]
        print(f"sdi{c}jah")
    elif(len(b)<3):
        d=b[1:]+b[0]
        print(d)

code()

# for decoding
def decode():
    g=input("enter the word:")
    if(len(g)>=3):
        e=g[0:-2]
        f=g[len(g):-3]
        print(f)
    # pass
decode()
        
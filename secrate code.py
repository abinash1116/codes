
#for coding
def code():
    b=input("enter the word:")
    if(len(b)>=3):
        c=b[1:]+b[0]    #b[1:]=index 1 dekhi paxadi ko sabai line but index 0 naline and b[0]=index 0 matra line aru naline
        print(f"sdi{c}jah")
    elif(len(b)<3):
        d=b[1:]+b[0] 
        print(d)



# for decoding
def decode():
    g=input("enter the word:")
    if(len(g)>=3):
        e=g[3:-3] #aagadi ko 3 oota exclude garera tespaxi ko leko ra paxadi ko 3 oota exclude garna -3(paxadi ko 3 oota hatako) gareko
        f=e[-1]+e[:-1] #e[-1l=ast ko character aagadi liyaixa and e[:-1] last ko bahek aru sabai character print garxa 
        print(f)
    elif(len(g)<3):
        h=g[-1]+g[:-1] 
        print(h)


a=input("if you want to code or decode??")

if a=="code":
    code()
else:
    decode()
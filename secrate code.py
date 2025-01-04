
#for coding
def code():
    b=input("enter the word:")
    if(len(b)>=3):
        c=b[1:]+b[0]    #b[1:]=it takes the character after index[1] and b[0]=takes the first character or the character from [0]index
        print(f"sdi{c}jah")
    elif(len(b)<3):
        d=b[1:]+b[0] 
        print(d)



# for decoding
def decode():
    g=input("enter the word:")
    if(len(g)>=3):
        e=g[3:-3] #it excludes first 3 character from the input and also exclude last 3 character from the input
        f=e[-1]+e[:-1] #e[-1]=takes the last character and e[:-1] takes all the character from the input excluding last character 
        print(f)
    elif(len(g)<3):
        h=g[-1]+g[:-1] 
        print(h)


a=input("if you want to code or decode??")

if a=="code":
    code()
else:
    decode()

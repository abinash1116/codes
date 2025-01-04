def sum(a,b):
    sum=a+b
    print(sum)

a=2
b=2
sum(a,b) #mathi lekheko function lai muni call gareko matra ho mathi sabai program lekhho ani tehe function lai call garera muni ren garna sakinxa names or arguments modify garera


def multiply(a , b):
    pass #pass lekhe paxi yo function paxi pani lekhna milxa yadi function define garyo ra tesma kunai program lekhena vane error aauna sakxa


def add(a=1 , b=3):
    print(a+b,"= sum")

add(a , b)

# 1)default arguments
def add(a , b): #we can also write the function in this way
    print(a+b,"= sum")

add(4 , 2)

def add(a=1 , b=3):
    print(a+b,"= sum")

add(8 , 2)   #yadi maile arguments lai aagadi nai initialize ya value assign gare ani feri muni function ma call garda arkai value assign gare vane program le muni assign gareko value linxa first ma initialize gareko value lidaina

def add(a=1 , b=3):
    print(a+b,"= sum")

add(4) #yeso garda mathi ko a ko value lai ignore garxa ra muni ko value linxa
add(b=2) #yeso garda mathi ko b ko value lai ignore garxa ra muni ko b ko value linxai


def average(*numbers): #aagadi * lekhe paxi hami le jati pani numbers halna pauxum arguments ma
    sum=0
    for i in numbers:
        sum=sum+i
    print("the average is ", int(sum/len(numbers)))

average(2 , 2, 2)
        

def average(*numbers): 
    sum=0
    for i in numbers:
        sum=sum+i
    return int(sum/len(numbers)) #return vaneko malai kun value return garnu xa thyakkai tehe display hune kura matra ho 

c=average(2 , 2 , 2) #j kura pani return huna aateko xa tyo sidhai gaera c ma store hunxa ani c ma vako value display garxa
print(c)
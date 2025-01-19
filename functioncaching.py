from functools import lru_cache

@lru_cache(maxsize=None)  
def fun(n): #in this lruchache function this returning function is saved already so wheneven we print fun(2) for the second time the value is already stored so it will give the result immidetiely
    return n*2 

print(fun(2))
print(fun(3))
print(fun(2))
print(fun(3))

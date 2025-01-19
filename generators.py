def generator():
    for i in range(10): #yo hami le aauta function ko structure ya design banako xum jun chai at the point chalauna milxa ra suru mai yesle data haru store gareko hudaina jaba hami run garxum ani matra data haru store garera run garxa
        yield i #yield is written to return the generator function and stops the execution until next request is given

g=generator()
print(next(g))


def my_generator(a):
    for i in range (5):
        return f"{a+i}"
gen=my_generator(1)
print(gen)
print(gen)
print(gen)
print(gen)
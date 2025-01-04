#str.format
name="abinash"
caste="oli"
country="nepal"
a="my name is {} {}. and I live in {}"
print(a.format(name,caste,country))

#f-string
name="abinash"
caste="oli"
country="nepal"
a=f"my name is {name} {caste}. and I live in {country}"
print(a)

b=f"my name is {{name}} {caste}. and I live in {country}" #if i want to display the output as my name is name then i have to use two braces simultaneously {{}}
print(b)
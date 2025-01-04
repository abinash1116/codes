dic={ 
    1:"ram",
    2:"shyam",
    3:"hari"
}
print(dic[3]) #this throws an error if the given key is not in the dictionary
print(dic.get(3)) #this gives null or none value if the given key is not in the dictionary

for key in dic.keys():
    print(f"the value corresponding to {key} is {dic[key]}") #this prints individual values  

dic={ 
    1:"ram",
    2:"shyam",
    3:"hari"
}
print(dic.items()) #this prints the whole items in the dictionary
for keys,values in dic.items():
     print(f"the value corresponding to {keys} is {values}") #this prints individual values  from the items


info={
     "abinash":"name",
     "oli":"caste",
    "nepal":"country"
}
info.update({"age":19}) #this updates or add the new item in the dictionary
print(info)

info={
     "abinash":"name",
     "oli":"caste",
    "nepal":"country"
}
info.clear() #this clears or empty the dictionary
print(info)

info={
     "abinash":"name",
     "oli":"caste",
    "nepal":"country"
}
info.pop("oli") #this removes the specified item from the dictionary
print(info)

info={
     "abinash":"name",
     "oli":"caste",
    "nepal":"country"
}
info.popitem()   #this remove sthe last item from the dictionary
print(info) 


# info={
#      "abinash":"name",
#      "oli":"caste",
#     "nepal":"country"
# }
# del info()
# print(info)  #this throws an error as output since del method deletes entire dictionary
#del info["oli"]
#print(info) #this deletes only oli item from info dictionary

user={
     "name":"abinash",
     "age": 19
}
print(f"{user["name"]} is {user["age"]} years old")


try:
    a=int(input("enter any number:"))
    print("multiplication")
    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")
except Exception as e:
    print("error occured")

print("code completed")

# try:
#     a = int(input("Enter any number: "))
#     for i in range(1, 11):
#         print(f"{a} X {i} = {a * i}")
# except ValueError:
#     print("Invalid input! Please enter a valid number.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")

# print("Code completed")




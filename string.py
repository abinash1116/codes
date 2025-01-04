name="abinash oli"
print(name[0:5])
print(len(name)) 
len1=len(name)
print("abinash is",len1 ,"letters word")
print(name[-5:-3])  
for i in name:
    print(i)
nm="Harry!!"
print(nm[-4:-2])
print(name.upper())  #changes the string to uppercase 
print(name.lower())  #changes the string to lowercase
print(name.strip())  #removes the white space before and after strings
print(nm.rstrip("!")) #removes the trailing character i.e., paxadi ko character remover garxa
print(name.replace("ab" ,"AB")) #replace the letters from the string
print(name.split(" ")) #splits the string and converts in the form of list 
print(name.capitalize()) #makes the first letter of the string capital 
print(name.center(50)) #aligns the strings to the center
print(name.center(50 ,".")) #aligns the strings to the center giving (.) to both leading and trailing position
print(len(name))
print(len(name.center(50))) #knowing how this center works it gives 50-11=39 space to the front i.e., 11 the length of string and remaining 39 infront and back of the string making the string to the center
print(name.count("a")) #it counts the number of times the letter or the character in the string is 
print(name.endswith("oli")) #it helps to know if the given string is getting end by the character or not
print(name.endswith("s",2,6)) #it helps to check if the string is ending with certain character between the given interval by the users first position i.e, 2 is counted but second position i.e., 6 is not counted 5 is counted so position from (2-5) is taken to consideration
print(name.find("a")) #it helps to find the character in the string and returns the index or the position of the string and if the character given by the user is not found then (-1) is returned
print(name.index("a")) #if the given character is not found while using index function then error is shown otherwise the work of index and find is same
print(nm.isalnum()) #helps to find if the given string is alphabet or number only characters from (A-Z),(a-z), and (0-9) is considered even the special characters are not taken into consideration
print(name.isalpha()) # it helps to find if the given string is only alphabets or not
print(name.islower()) #it helps to check whether all the characters in the strings are in lowercase or not
print(name.isprintable()) #it helps to return is all the string is prinatable or not is any escape character like (\n) or (\t) is given then it will return false
print(name.istitle()) #helps to check whether all the characters have first letter captial or not
print(name.isupper()) #helps to check if all the characters in the string are upper case or not
print(name.startswith("a")) #checks whether the following string starts with the given character or not and it is case sensative i.e., if a is written as A then it will given false as output
print(name.swapcase()) #converts all the lowercase string or uppercase and vice versa
print(name.title()) #makes all the first letter of the characters in the string capital
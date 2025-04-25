string = input("Please enter a string: ")
string2 = ('')
for i in string:
    string2 = i + string2

print("/nThe Original string is: ", string)
print("The Reversed string is: ", string2)
str1 = input("Enter string1: ")
str2 = input("Enter string2: ")

str1 = str1.lower()
str2 = str2.lower()

if sorted(str1) == sorted(str2):
    print("True")
else:
    print("False")
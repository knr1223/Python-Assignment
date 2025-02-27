str = input("Enter a string: ")
char = input("Enter the character to check: ")

starts_with = lambda s, c: s.startswith(c)

print(starts_with(str, char))
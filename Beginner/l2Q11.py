string_list = input("Enter words separated by commas: ")
words = string_list.split(',')
words = [word.strip() for word in words]

result = list(map(list, words))

print(result)
list1 = list(map(int, input("Enter a list of numbers: ").split()))

def unique_elements(input_list):
    return list(set(input_list))

print("List with unique elements:", unique_elements(list1))
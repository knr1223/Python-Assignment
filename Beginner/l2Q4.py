input_arr = list(map(int, input("Enter a list of numbers: ").split()))
D = int(input("Enter the number of rotations: "))

n = len(input_arr)
D = D % n # to manage if D more tha n
rotated_arr = input_arr[-D:] + input_arr[:-D] # used slicing

print("Array after rotation:", rotated_arr)
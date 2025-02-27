l1 = [1, 2, 3, 4, 5]

index = int(input("Enter the index to modify: "))
value = int(input("Enter the new value: "))

try:
  l1[index] = value
  print(f"Updated list: {l1}")
except IndexError:
  print("Error: Index is out of range! Please enter a valid index.")
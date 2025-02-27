l1 = list(map(int, input("List 1: ").split()))
l2 = list(map(int, input("List 2: ").split()))

common_elements = list(set(l1) & set(l2))# using intersection

print("Common elements:", common_elements)
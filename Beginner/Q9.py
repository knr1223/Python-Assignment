l1 = [1, 2, 3, 2, 4, 1, 2, 4, 5]

frequency = {}

for i in l1:
  if i in frequency:
    frequency[i] += 1
  else:
    frequency[i] = 1

print("Frequency count:", frequency)
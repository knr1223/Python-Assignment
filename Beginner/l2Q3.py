input_arr = list(map(int, input("Enter a list of numbers: ").split()))
k = int(input("Enter the value of K: "))

pair_count = 0
for i in range(len(input_arr)):
  for j in range(i+1, len(input_arr)):
    if input_arr[i] + input_arr[j] == k:
      pair_count += 1

print("Pair count:", pair_count)
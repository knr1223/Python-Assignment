l1= list(map(int, input("Enter numbers: ").split()))

def find_median(l1):
  l1.sort()
  n = len(l1)
    
  if n % 2 == 1:
    return l1[n // 2]
  else:
    mid1, mid2 = l1[n // 2 - 1], l1[n // 2]
    return (mid1 + mid2) / 2

median = find_median(l1)
print(f"Median: {median}")
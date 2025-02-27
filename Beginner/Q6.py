num = int(input("Enter a number: "))

sum_of_divisors = 0

if num <= 0:
  print("Please enter a positive integer.")
else:
  for i in range(1, num):
    if num % i == 0:
      sum_of_divisors += i

if sum_of_divisors == num:
  print("Yes")
else:
  print("No")
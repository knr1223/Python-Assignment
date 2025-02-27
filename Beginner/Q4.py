num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = 0

for i in range(num1,num2+1):
  if i > 0 and i % 2 != 0:
    sum += i

print(f"Sum of odd numbers: {sum}")
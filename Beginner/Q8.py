num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

greater = max(num1, num2)
smallest = min(num1, num2)
for i in range(greater, num1*num2+1, greater):
  if i % smallest == 0:
    lcm = i

print(f"The LCM of {num1} and {num2} is {lcm}")
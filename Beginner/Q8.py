num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

max_num = max(num1, num2)

lcm = max_num

while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += max_num

print(f"LCM of {num1} and {num2} is: {lcm}")
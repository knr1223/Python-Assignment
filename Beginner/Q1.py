n = int(input("Enter a number: "))
if n % 3 == 0 and n % 5 == 0:
  print("Consultadd - Python Training")
elif n % 3 == 0:
  print("Consultadd")
elif n % 5 == 0:
  print("Python Training")
else:
  print("Number is not divisible by 3 or 5.")
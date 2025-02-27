num = int(input("Enter a number: "))
def is_power_of_two(n):
  if n == 1:
    return True
  if n <= 0 or n % 2 != 0:
    return False
  return is_power_of_two(n // 2)

result = is_power_of_two(num)
if result:
    print(f"{num} is a power of two.")
else:
    print(f"{num} is not a power of two.")
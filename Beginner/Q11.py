num = int(input("Enter a number: "))

while num >= 10:
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    print("Intermediate Sum:", sum)
    num = sum

print("Final Output:", num)
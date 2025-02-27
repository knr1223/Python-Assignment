str = input("Enter a string: ")

alphabet_count = 0
digit_count = 0

for char in str:
    if char.isalpha():
        alphabet_count += 1
    elif char.isdigit():
        digit_count += 1

print(f"Alphabets: {alphabet_count} & Numbers: {digit_count}")
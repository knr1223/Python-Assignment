user_input = input("Enter your encoded string: ")

def parse_encoded(encoded_str):
  parts = list(encoded_str.split('0'))

  return {
    "first_name": parts[0],
    "last_name": parts[1],
    "id": parts[2]
  }

parsed_data = parse_encoded(user_input)

print("\nParsed Data:")
print(parsed_data)

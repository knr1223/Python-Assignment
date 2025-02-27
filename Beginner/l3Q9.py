user_input = input("Enter a string: ")

def encoding(input_str):
  encoded_str = ""
  count = 1

  for i in range(1, len(input_str)):
    if input_str[i] == input_str[i - 1]: #check if same as previous char
      count += 1
    else:
      encoded_str += input_str[i - 1] + str(count)  
      count = 1

  encoded_str += input_str[-1] + str(count)

  return encoded_str



encoded_output = encoding(user_input)

print("\nRun-Length Encoded String:")
print(encoded_output)

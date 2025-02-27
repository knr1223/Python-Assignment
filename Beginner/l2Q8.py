str = input("Enter a string: ")

def count_vowels(string):
  vowels = "aeiouAEIOU"
  count = 0
    
  for char in string:
    if char in vowels:
      count += 1
     
  return count

vowels_count = count_vowels(str)
print(f"Number of vowels: {vowels_count}")
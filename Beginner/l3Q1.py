import os

def even_length_words(file_path):
  with open(file_path, 'r') as file:
    lines = file.readlines()

  even_length_lines = []
  for line in lines:
    words = line.strip().split()
    even_words = [word for word in words if len(word) % 2 == 0]
    even_length_lines.append(" ".join(even_words))

  return "\n".join(even_length_lines)

script_directory = os.path.dirname(os.path.abspath(__file__))  # using this because i'll be pushing this ti github and not just run in local

file_path = os.path.join(script_directory, "doc.txt")  

output = even_length_words(file_path)
print(output)
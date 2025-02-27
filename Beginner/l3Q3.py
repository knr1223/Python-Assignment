import os

def JtoI(file_path):
  with open(file_path, 'r') as file:
    content = file.read()
  corrected_content = content.replace('J', 'I')

  print("Corrected Content:\n")
  print(corrected_content)

script_dir = os.path.dirname(os.path.abspath(__file__))#absolute path for file

file_path = os.path.join(script_dir, "words.txt")

JtoI(file_path)

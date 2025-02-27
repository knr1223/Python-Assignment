import os

def count_lines_in_file(file_path):
  with open(file_path, 'r') as file:
    line_count = sum(1 for line in file)

  return line_count

script_dir = os.path.dirname(os.path.abspath(__file__)) #getting absolete path

file_path = os.path.join(script_dir, "demo.txt")

line_count = count_lines_in_file(file_path)
print(f"Total number of lines in {file_path}: {line_count}")

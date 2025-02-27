students = ["Sam", "Alice", "Mona"]
subjects = ["Commerce", "Science", "Computer"]

mapped_dictionary = {}
for i in range(len(students)):
  mapped_dictionary[students[i]] = subjects[i]
print("Using for loop:", mapped_dictionary)

# Using dictionary comprehension
dict_comp = {students[i]: subjects[i] for i in range(len(students))}
print("Using dictionary comprehension:", dict_comp)

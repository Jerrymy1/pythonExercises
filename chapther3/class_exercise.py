

'''
from pathlib import Path

# creating folder by writing the program

file_path = Path.cwd()/"my_folder"
print(file_path)


file_path.mkdir(exist_ok=True)
new_file_path = file_path / "my_file.txt"
new_file_path.touch()
print(file_path.exists())
print(file_path.exists())
'''


'''value = "function"
for c_14 in value:
    print("hello")'''


variable = 'Hello boss baby'

for i in range(len(variable)):
    if variable[i] == "b":
        print(f"{variable[i]} found at index {i}")






word = 'Hello boss baby'

for index, value in enumerate(word):
 # for index in range(len(word)):
 print(value)



for i in range(len(word)):
 if word[i] == "b":
     print(word[i])
if word[i] != "b":
     print(word[i])









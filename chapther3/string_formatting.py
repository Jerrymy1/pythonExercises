'''
name = "Aliyah"
age = 20.567

#print(name, "is", age, "years old")
#s = "{} is {} yreas old" . format(name, age)
#s = "{1} is {0} yreas old" . format(age, name)

#s = "{0:<20} is {1} years old, and {0} loves {2}".format(name, age, "Java")
#s = "{0:^<20} is {1:>10.2f} years old, and {0} loves {2}".format(name, age, "Java")
#s = f"{name=:-^20}is{age:>10.2%} years old, and {name} loves {'Java'}"
#print(s)

#hello = "hello world"

for index, letter in enumerate(hello, start=1):
   print(f"{letter} --> {index}")


#for index in range(len(hello)):
 #   print(f"{hello[index]} --> {index}")


for i in range(1, 21, 2):
    s = "*" * i
    print(f"{s:20}{s:^20}{s:>20}")
    '''


'''A = "knight's"
B = 'knight\'s'
print (A)
print(B)
'''


s = 'hello world'
to_be_found = "d"
'''
for i in range(len(s)):

    if s[i] == to_be_found:
        print(f"{s[i]} was found at index {i}")
        break

else:
    print(f"Sorry i could not find your {to_be_found}")
'''


for index, char in enumerate(s):
    if char == to_be_found:
        print(f"{char} found at index {index}")
        break
else:
    print(-1)
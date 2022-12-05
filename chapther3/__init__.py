hello = "Hello there!!!"

#print(hello.find("e", 3, 5))
'''
found = 0
while True:
    found = hello.find("e",found)
    if found == -1:
        break
    print(found)

    found += 1

    print(hello.lower().count("e"))

print(hello.center(20, "*"))
print(hello.ljust(20, "*"))
print(hello.rjust(20, "*"))
'''


for i in range(1, 21, 2):
    asterisk = "*" * i
    print(asterisk.center(20))

print (hello.startswith("h"))
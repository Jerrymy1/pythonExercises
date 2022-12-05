count = 0
largest_num = 0
smallest_num = 0
second_num = 0

while count < 5:
    input_num = int(input("Enter a number"))

    if input_num > largest_num:
        second_num = largest_num
        largest_num = input_num

    if input_num < smallest_num:
        smallest_num = input_num


        count +=1

        print("The first largest number", largest_num)
        print("The second largest number", second_num)
        print("The first largest number", smallest_num)





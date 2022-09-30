import math
first_number = input("Enter the first number:")
second_number= input("Enter the second number:")
third_number = input("Enter the third number:")
forth_number = input("Enter the forth number:")
fifth_number = input("Enter the fifth number:")

array = [first_number,second_number,third_number,forth_number,fifth_number]

max_num = 0
min_num = 0

if int(first_number) < int(second_number):
    max_num = second_number
    min_num = first_number
elif int(first_number) > int(second_number):
    max_num = first_number
    min_num = second_number

if int(max_num) < int(third_number):
    max_num = third_number
elif int(max_num) > int(third_number) and int(third_number)< int(min_num):
    min_num = third_number

if int(max_num) < int(forth_number):
    max_num = forth_number
elif int(max_num) > int(forth_number) and int(forth_number)< int(min_num):
    min_num = forth_number

if int(max_num) < int(fifth_number):
    max_num = fifth_number
elif int(max_num) > int(fifth_number) and int(fifth_number)< int(min_num):
    min_num = fifth_number

print("Max Number: " + str(max_num))
print("Min Number: " + str(min_num))
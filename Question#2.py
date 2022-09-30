first_num=input("Inter the first number:")
second_num=input("Inter the second number:")

import math

if first_num.isdigit()== True and second_num.isdigit()== True:
    pass
else:
    print('error')

first_input = int(first_num)
second_input = int(second_num)

print("1_+ \n2_- \n3_* \n4_/ \n5_^ \n6_%")
first_operation=input("the operation you want")
result=0
if first_operation=="1" or first_operation=="+":
    result=first_input+second_input
    print(result)
elif first_operation=="2" or first_operation=="-":
    result=first_input-second_input
    print(result)
elif first_operation=="3" or first_operation=="*":
    result=first_input*second_input
    print(result)
elif first_operation == "4" or first_operation == "/":
    result = first_input / second_input
    print(result)
elif first_operation == "5" or first_operation == "^":
    result = first_input ** second_input
    print(result)
elif first_operation == "6" or first_operation == "%":
    result = first_input % second_input
    print(result)
else:
    print("error")

print("1_round \n2_floor \n3_ceil \n4_without,comma \n5_exit")
seconed_operation=input("put the second operation")
if seconed_operation == "1" or seconed_operation== "round":
    print(round(result))
elif seconed_operation=="2" or seconed_operation=="floor":
    print(math.floor(result))
elif seconed_operation=="3" or seconed_operation=="ceil":
    print(math.ceil(result))
elif seconed_operation=="4" or seconed_operation== "without,comma":
    print(int(result))
elif seconed_operation=="5" or seconed_operation=="exit":
    print("byebye")
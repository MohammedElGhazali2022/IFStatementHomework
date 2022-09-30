name = input("Enter your name:")
age = input("Enter your age:")
address = input("Enter your address:")

if name.isdigit() or name.isspace():
    print("error")

elif age.isdigit()== False or age.isspace():
    print("error")

elif address.isdigit() or address.isspace():
    print("error")
else:
    print(f"Hello Mr/Ms {name} age {age} located in {address}. \n thanks for beening one of our community,    enjoy")




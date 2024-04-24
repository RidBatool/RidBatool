a = input("enter your password containg 7 to 8 character and at least one numeric digit and a special character:")
if 7<=len(a)<=15 and any(char.isdigit() for char in a) and (not char.isalum() for char in a):
    print("acceptable");
else:
    print("Try again");

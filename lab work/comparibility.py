st1=input("Enter first string: ")
st2=input("Enter second string: ")
if len(st1)!=len(st2):
    print("These are not comparable")
else:
    for i in range(len(st1)):
        if st1[i]==st2[i]:
            print("Common")
        else:
            print("Uncommon")

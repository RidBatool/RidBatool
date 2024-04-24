while True:
    n=int(input("enter your number:"))
    n2=int(input("enter you second number"))
    ope=int(input("enter operat\n1.add\n2.sub\n3.mul\n4.divide"))
    if ope==1:
        print(n+n2)
    elif ope==2:
        print(n-n2)
    elif ope==3:
        print(n*n2)
    elif ope==4:
        print(n/n2)

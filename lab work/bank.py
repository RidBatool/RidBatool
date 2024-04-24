while True:
    id=input("Enter your ID; ")
    print(id)
    print("Main Menu")
    print("***********")
    print("1.Deposite Money.\n2.Withdraw Amount\n3.Login as Different User")
    choice=int(input("Select your choice: "))
    if choice==1:
        print("money is deposited")
    elif choice==2:
        print("amount is withdraw")
    elif choice==3:
        print("Successfully login")
    a= input("If you want to continue press y/Y")
    if a!="Y"or a!="y":
        break
    

list = []
print("welcome to this platform")
while True:
    choice = int(input("enter ypour choice: "))
    if choice == 1:
        date = input("date: ")
        catgory = input("karcha (food ,mack,book): ")
        detail = input("detail: ")
        amount = float(input("total amount: "))
        
        karcha = {
            "date": date,
            "catgory": catgory,
            "detail": detail,
            "amount":amount
        }
        list.append(karcha)
        print("your detail add sucessfully")
    elif choice == 2:
        if (len(list)== 0):
            print("add karcha...")
        else:
            count = 1
            for eachkarcha in list:
                print(f"karcha no {count} -> {eachkarcha["date"]}, {eachkarcha["catgory"]},{eachkarcha["detail"]}, {eachkarcha["amount"]}")
                    
    elif choice == 3:
        total = 0
        for eachkarcha in list:
            
            total = total + eachkarcha["amount"]
        print ("THE TOTAL KARCHA IS : ",total)
        
    elif choice == 4:
        print("thanku for visiting ,vesite again..!")
        break
    else:
        print("Invailed inpt...!")
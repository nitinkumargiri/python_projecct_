def calculator():
    try:
        num = float(input("enter your first number:"))
        num1 = float(input("enter your second number: "))
        
        print("1. addition ")
        print("2. substraction")
        print("3. mulktiplication")
        print("4. division")
        
        choice = input("enter your choice: ")
        
        if choice == '1':
            print("Result: ",num + num1)
            
        elif choice == '2':
            print("Result: ",num - num1)
            
        elif choice == '3':
            print("Result: ", num * num1)
        elif choice == '4':
            
            try:
                print("Result: ",num / num1)
            except ZeroDivisionError:
                print("ERROR: Division by zero...!")
        else:
            print("Invailed choice........!")
             
    except ValueError:
        print("ERROR plese enter vailed number.")
    
    except Exception as e:
        print("unexception error..!")
        
        
calculator()
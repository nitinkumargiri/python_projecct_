def add(a , b):
    return a + b

def substaction(a , b):
    return a - b

def multiply(a , b):
    return a * b

def devision(a , b):
    if b == 0:
        print("ERROR...! Divided by Zero..!")
        
    else:
        return a / b
    
print("1. addition")
print("2. substraction") 
print("3. multiplication")
print("4. division")
print("5. exit")

while True:
    choice = int (input("enter your choice : "))
    num1 = float(input("enter your first choice: "))
    num2 = float(input("enter your second choice: "))
    
    if choice == 1:
        print("Result: ",add(num1 , num2))
        
    elif choice == 2:
        print("Result : ",substaction(num1 , num2))
        
    elif( choice == 3):
        print ("Result : ",multiply(num1, num2))
        
    elif choice == 4:
        print("Result: ",devision(num1, num2))
        
    else:
        if choice == 5:
            print ("have a good day..!")
            break
        else:
            print("Invailed choice..!") 
        

        
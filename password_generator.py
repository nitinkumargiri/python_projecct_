import random

def get_password_length(length):
    character = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
    password = ""
    
    for i in range(length):
        password += random.choice(character)
        
    return password

while True:
    
    print("WELCOME TO PASSWORD GENERATOR PLATFORM.")
    print("write__ Exit __ to come out ")
    
    length = int(input("enter your length of password: "))
    
    password = get_password_length(length)
    print("your generated password is : ",password)
    
    choice = input("Do you want to know another password(yes/no): ")
    
    if "yes" in choice.lower():
        #choices = input("Do you want to know another password(yes/no): ")
        continue
    
    else:
        print("HAVE A GOOD DAY! Visit Again..!")
        break
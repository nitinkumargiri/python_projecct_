import random
import time

otp = random.randint(100000,999999)
expiry_time = 10

print("your otp is : ",otp)
start_time = time.time() 

user_otp = input("enter otp withen 10 second: ")
end_time = time.time()

if end_time - start_time > expiry_time:
    print("otp is expired❌❌")
elif user_otp == str(otp):
    print("otp enter sucessfully✅✅✅")
else:
    print("Invailed otp..!❌❌❌❌❌⚔️⚔️")

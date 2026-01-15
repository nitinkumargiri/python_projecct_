f = open("student.txt", "a")

roll = input("ENTER roll number : ")
name = input("enter your name : ")
mark = input("enter your marks : ")

f.write(roll + " " + name + " " + mark + "\n")
f.close()

print("record saved successfully.✅")

print("STUDENT RECORDS")
f = open("student.txt", "r")
print(f.read())
f.close
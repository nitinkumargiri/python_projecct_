
print(" THE PWELCOME TOYTHON CHATBOT")

print ("you enter bye or exit to end it.")

data = {
    "hi":"hi,what's going on","who are you":"i am a smart chatbot",
    'who':'i am a chatbot',"how are you":"i am fine, thank you","what is your name":"i am called chatbot",
    }

def my_function(user_question):
    user_question = user_question.lower()
    for eachkey in data:
        if eachkey in user_question:
            return data[eachkey]
        
        return "i am not able to tell that yet, i am still in learning mode"
    
while True:

        userinput = input("you: ")
        reply = my_function(userinput)

        print("Bot: ",reply)

        if "bye" in userinput or "exit" in userinput.lower():
            print ("Bot : bye have a nice day..!")
            break



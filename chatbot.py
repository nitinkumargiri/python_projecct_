#Rule Based AI Python ChatBot 

import datetime
import time

name= input("Swagat h, enter your name : ")
presentHour= datetime.datetime.now().hour

if 5 <= presentHour <= 11: 
    print("Good morning, ", name)
elif 11 <= presentHour <= 17:
    print("Good afternoon, ", name)
elif 17 <= presentHour <= 20:
    print("Good evening, ", name)
else:
    print("Good night, ", name)



print("Namaste! Welcome to Your ChatBot")
print("You can ask me basic question, Type 'bye' to exit from the bot\n")

# Chatbot Memory Creation [ dictionary of responses ]

responses = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am very fine. Thank you",
    "who are you": "I am smart AI chatbot",
    "motivate me": "Keep going. Every bug of your project makes you a better developer",
    "happy": "Great to hear that",
    "functions kya hote hai": "jakar chapter 7 padho",
    "hello" "hi":"Hlw how may i help you ?",
    "hlo": "Hey there! How's it going??",
    "hlw":  "hello What's up?",
    "hii": "hlo what's up ?",
    "how are you": "I'm good, thanks for asking..  what about you?",
    "good": "Good to hear this.. How can i help you 🤔?",
    "excellent": "wow.. looks like you are energetic right now 😎\nhow can i help you 🤔 ?",
    "sing a song": "i can't, i am a virtual chatbot created By RVA , so i can only give you answers of some questions",
    "nothing": "umm.. okk ☺️",
    "can you talk": "i can't, i am a virtual chatbot created By RVA , so i can only give you answers of some questions",
    "what are you doing": "just talking to you..😇",
    "who made you": "i am created by RVA,owner: adarsh singh",
    "what is your origin": "india",
    "what is your name": "i'm Goldy(RVA)",
    "who is your owner": "my owner is Mr. Adarsh singh",
    "who is richest man on earth": "Elon musk",
    "who is founder of facebook": "mark juckerburg",
    "who is ceo of google": "sunder pichai",
    "what can you do": "I can give do like greetings, some facts, motivatio, some python programs(addition)(subtraction) and other..feel free to ask..☺️",
    "what you can do": "I can give do like greetings, some facts, motivatio, some python programs(addition)(subtraction) and other..feel free to ask..☺️",
    "2+2": "4",
    "what is the value of pi": "22/7 or 3.14",
    "in a company what major roles are there": "in a company there are majoraly 5 positions which are very important for a company constant growth\n1. Ceo\2.Coo\3.Cmo\4.Cfo\5.Cto these are the top and valuable position in a majoraly tech company",
    "tell me a joke": "your life... ☠️", 
    "what is the full form of NEP": "full form of NEP is national education policy",  
    "tell me a dark joke": "dark humour is like food everyone can't gets it...☠️",
    "what is the one motivaion you give": "you only have 2 options: \n 1. Either play safe and die with regrets or \n 2. Take risk and die with a story",
    "what is the criteria to vote in india": "to vote in india you have to be 18 or plus",
    "can you solve math problems ?": "yeah bit very basic..",
    "what is 4 * 5": "20",
    "what is 100/5": "20",
    "give me some motivation": "sure:\nif you start...one thing is for sure you will not die with regret\nso just do it.. hope this give you a boost 😊",
    "i want to start a business what should i do":"pick something research about it and just start..good luck",
    "tell me an idea that can really go big": "sure: \n Pharmacy\n makeup for women\n agriculture new technogies\n low rate clother with good quality",
    "thanku": "wlcm have a nice day ☺️",
    "thanks": "most welcome ☺️ feel free to ask anything..",
    "what is the diameter of earth": "the diameter of earth is approximately 12742 kilometer.",
    "what do you think about ai": "ai is really great and it will gonna boost very much because of its capablities...",
    "create a python code of subtraction": "sure: \n def subtract(): \n inp = input('enter first number': )\n inp2= input('enter second number': )\n sub = inp - inp2\n print(sub)\n subtract())",
    "can you recommend me a book": "hard things by hard things, this book is really good.",
    "can you dance": "i can't, i am a virtual chatbot created By RVA , so i can only give you answers of some questions",
    "who is highest followed person on instagram": "cristiano ronaldo is highest followed person on instgram",
    "who is the goat of football": "cristiano and messi both are goat players..of football",
    "choose one": "messi because he have a world cup but, cristiano is also a very high goated player respect 🫡",
    "tell me one thing that can change my life": "just take risk and see the outcome you will never regret",
    "can you do calculations": "yes but a little bit",
    "can you speak": "i can't, i am a virtual chatbot created By RVA , so i can only give you answers of some questions",
    "who created you": "i am created by RVA owner Adarsh kumar singh",
    "tell me about your owner information":  "'sorry' i can't disclose my owner info or any other person's info as it's private thing 🙂",
    "what you can do that other ai cant": "for your clarification i am not an AI i am just a normal chatbot which can give answers of simple questions..",
    "tell me another joke": "Why did the astronaut break up with his girlfriend? \n Because he needed space!",
    "emoji": "😀😃😄😆🥹😅😂🤣🥲☺️😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🥸🤩🥳🙂‍↕️😏😒🙂‍↔️😞😔😔😟😕🙁☹️😣😖😫😩🥺😢😭😤😠😡🤬🤯😳🥵🥶😶‍🌫️😱😨😰😥🤗🤔🫣🤭🫢🫡🤫🫠🤧🤤😑🫤",
    "give me some happy emoji": "sure:\n😀😃😄 ☺️😊😇", 
    "give me some sad emoji": "sure:\n🥹😒😞😔😔", 
    "i am sad": "ohh..don't be sad 🥹\n here is a joke that can make you smile and make your day better ☺️😊\n Why don't skeletons fight each other?\nBecuse they don't have the guts! 😄\nHope that gave you a laugh!",
    "i am happy": "That's awesome!😊", 
    "who is goat of cricket": "Sachin Tendulkar is often called the God of Cricket.",
    "describe yourself in one word": "helper",
    "can you describe yourself in one word": "helper", 
    "who is rva": "sorry i can't disclose this information now..😊but soon...",
    "what is the full form of ceo": "full form of ceo is cheif executive officer.",
    "what is rva": "sorry i can't disclose this information now..😊 but soon...", 
    "what is the meaning of rva": "sorry i can't disclose this information now..😊 but soon...",
    "tell me about yourself": "sure, I'm Goldy created by Rva and i answer some questions...and\n something big is coming soon..😎",
    "how to become a developer": "Becoming a developer is an exciting journey! Here's a general roadmap to help you get started:\n1. Choose Your Path\n2. Learn the Basics of Programming\n3.Get Hands-On with Projects \nbest of luck for your future😊",
    "okk": "☺️", 
    "ok": "☺️",
    "okay": "",
    "yes": "hmmm🙂", 
    "who is Prime Minister of india": "Prime Minister of india is shree narendra damodar das modi jee",
    "create a python code of addition": "sure: \ndef add(): \ninp = input('enter first number': )\ninp2= input('enter second number': )\nsum = inp + inp2\nprint(sum)\nadd())",
    "create a python code of multiplication": "sure: \ndef multiply(): \ninp = input('enter first number': )\n inp2= input('enter second number': )\nmul = inp * inp2\nprint(mul)\nsubtract())",
    "create a python code of division": "sure: \ndef division(): \ninp = input('enter first number': )\n inp2= input('enter second number': )\ndiv = inp / inp2\nprint(div)\ndivision())",
    "can you recommend me a book": "hard things by hard things, this book is really good.",
    "can you code": "yeah a little like i can give you basic code for addition , subtraction and multiplication and division.. more coming soon..☺️ 😊(type this:  create a python code of :whatever you want)",
    "can you write code": "yeah a little like i can give you basic code for addition , subtraction and multiplication and division.. more coming soon..☺️ 😊(type this:  create a python code of :whatever you want)",
    "what is noun": "noun is a naming word, person place or thing",
    "what is adjective": "adjective is a word that describe noun or pronoun",
    "which is the highest polluted city in india ?": "delhi",
    "which is the cleanest city in india": "indore(madhya pradesh).",
    "how many states in india": "28 states",
    "tell me some interesting fact": "Sharks existed before trees!🥸",
    "when you were created": "i was created on March 01/2025",
    "what is your aim": "my aim is to provide answers of your questions..",
    "how many days in a months": "Well it depends 30 or 31 and february has 28 and in leap year 29.",
    "how can i focus on one thing": "by meditation🧘\nmeditation really help to improve mind and it really increase your ability to focus🧿",   
    "which is the fastest programming language": "well c and c++ are considered as fastest programming language.",
    "which is faster python or c": "c but python is more powerful becuase it has so much use in ai and different fields also",
    "you are wrong": "i am basic chatbot so maybe i can be wrong sometime",
    "what is the reason behind creating you" : "as of my owner\ni was created just for some pratice of code ☺️",
    "what is python": "python is highly used prgramming language which is used to make applications ai intergrated chatbots and many..",
    "why we need to understand programming language": "well, to communicate with computer.", 
    "what is the capital of india": "delhi is the capital of india.",
    "what should i learn so that my future will be secure": "so learning is very curcial part in life\nif you want to secure future you should take any carrer (you are interseted in)\nand research about that thing and fully prepare for that \nthis can make you future secure and also helps to go with your desire destination 😊",
    "what is the full form of seo": "search engine optimisation", 
    "what are the skills required to build website": "sure:\nfirst you need to learn fornt-end part (html, css javascript) and next js\nfor backend you have to learn node js\nfor user data learn mongodb\nand you are ready to deploy a fully functioned web\nand in last you need your domain name and vps.\n that's all you need 😊\n hoping best for your future 😊😊",
    "what are the skills required to build a fully working website": "sure:\nfirst you need to learn fornt-end part (html, css javascript) and next js\nfor backend you have to learn node js\nfor user data learn mongodb\nand you are ready to deploy a fully functioned web\nand in last you need your domain name and vps.\n that's all you need 😊\n hoping best for your future 😊😊",
    "what are the skills required to build websites": "sure:\nfirst you need to learn fornt-end part (html, css javascript) and next js\nfor backend you have to learn node js\nfor user data learn mongodb\nand you are ready to deploy a fully functioned web\nand in last you need your domain name and vps.\n that's all you need 😊\n hoping best for your future 😊😊",
    "which is the best ipl team": "well all are very good teams but\naccording to trophies\nMI and CSK are the best teams so far",
    "which mobile phone is best": "according to survey of 2024 samsung s24 is the best mobile phone",
    "which mobile is best": "according to survey of 2024 samsung s24 is the best mobile phone",
    "give me some motivational lines": "sure:\nno is going to save you\nif you want to create a big impact on world start working\nexcution is the main thing,\neveryone has an idea but few people have courage to execute so start executing things,\ndon't afraid of failing ",
    "what is the formula of perimeter of rectange": "2*(l+b)",
    "what is the area of rectangle": "l * b",
    "which is the tallest bridge in world?" : "tallest bridge in world is chenab bridge in india inaugurated in june 2025",
    "recommend my a book": "Hard things about hard things or 'zero to one'",
    "how can i become billionaire" : "you have seen alot of motivation earlier  so am not goona give you any kind of motivation\ni will tell you a fact that most people know but they don't apply\nif you really want to become billioaire\ntake an idea learn first and exceute that idea\nif that idea doesn't worked try other until succesfull\nso take action\nyou wil definetly not regret",
    "what is the full form of who": "full form of who is world health organization", 
    "how many types of machine learning are": "there are 3 types of machine learning.\n1.supervised ml\n2.unsupervised ml.\n3.reinforcement ml",
    "what language do i require to enter in machine learning": "1st: 'Python' it is a base language.\n2.python's 4 libraries you have to study\(1):Numpy\(2):Pandas(3).matplotlib\(4).seaborn\nand in last you need to undetstand sklearn\nit is very important fot ml models and all\nso you need basic knowledge how we import what is the use\nfter all that\you are ready to dive into ml\nbest of luck champ😊",
    "which planet is closest to the sun": "Mercury is the planet closest to the Sun, with an average distance of about  58 million kilometers", 
    "we are in which galaxy": "We are in milkyway galaxy.",
    "tell me the full form of ros": "full form of ros is robotics operating system"

} 

# Method/Function to get response of ChatBot 

def getResponseOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to tell that yet. I am still in learning mode."    
    

# Take user input 


while True:
    userInput= input("Please ask your question: ")
    reply= getResponseOfBot(userInput)
    print("Bot Response: ", reply)

    if "bye" in userInput.lower() or "exit" in userInput.lower():
        print ("have a nice day.")
        break
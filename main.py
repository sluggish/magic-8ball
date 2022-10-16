import random
import time

answers = ["It is certain!",
           "It is decidedly so", 
           "Without a doubt!", 
           "Yes Definitely", 
           "You may rely on it", 
           "As I see it, yes!",
           "Most likely", 
           "Outlook Good!",
           "Yes!",
           "My signs are pointed to yes!",
           "Reply hazy, try again",
           "Ask again later",
           "Better not tell you now",
           "Cannot be predicted right now",
           "Don't count on it",
           "My reply is no",
           "My sources say no",
           "Outlook is not so good",
           "Very Doubtful!"
        ]

def Main():
    input("What is your question? ")
    print("Magic 8 ball is thinking...")
    time.sleep(5)
    Respond()

def Respond():
    print(random.choice(answers))

Main()
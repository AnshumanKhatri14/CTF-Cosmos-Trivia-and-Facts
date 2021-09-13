# this is where all the funcs needed for main.py will be

import csv
from os import extsep
import random
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate", 178)

# Files Needed To Be Read

ques_file=open("questions.csv")
read_ques_file=csv.reader(ques_file)
global ques
ques=[]         # 1-Q, 2-O1, 3-O2, 4-O3, 5-O4, 6-A
for x in read_ques_file:
    ques.append(x)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def quiz():      # Function To Start Another Quiz
    print("Do you want to start the quiz? (Yes/No): ")           # Ask If Want To Take One More Quiz Or Not
        
    talk("Do you want to start the quiz? (Yes or No)")
        
    inp=input().upper()
    if inp=="Y" or inp=="YES":
        for ques_no in range(1,6):      # Number Of Questions To Be Asked In Each Quiz
            r=random.randint(1,20)   # Random Questions From The List (Also, Set The Range)
            ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]     # Assigning Variables To All The Options

            print(f"\nQuestion {str(ques_no)}: {ques[r][1]}\n 1. {ques[r][2]}\n 2. {ques[r][3]}\n 3. {ques[r][4]}\n 4. {ques[r][5]}")    # Displaying Question Along With Options
            talk(f"\nQuestion {str(ques_no)}: {ques[r][1]}\nThe options are:\n first, {ques[r][2]}\n second, {ques[r][3]}\n third, {ques[r][4]}\n and fourth, {ques[r][5]}")
                        
            check_quiz_ans(answer="",r=r,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4)  # Calling Function To Check The Answer
        home()
    
    else:
        home()  # FOR NOW Exit 

def check_quiz_ans(answer,r,ans1,ans2,ans3,ans4):    # Function To Take And Check The Answer
    print("\nEnter you answer (option 1, 2, 3, or 4) or enter 'stop' to exit the trivia: ")
    talk("Enter the correct option number ")
    
    answer=input()    # Input
    if (answer=="1" and ans1!=ques[r][6]) or (answer=="2" and ans2!=ques[r][6])\
        or (answer=="3" and ans3!=ques[r][6]) or (answer=="4" and ans4!=ques[r][6]):       # If Answer Wrong
        print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ques[r][6]}.")
        talk(f"\nYour answer is incorrect.\nThe correct answer to this question is; {ques[r][6]}.")
    
    elif answer.lower() == "stop":
        home()

    else:
        print("\nYour answer is correct!")    # If Answer Right
        talk("Your answer is CORRECT!")

def rapid_fire():
    talk("Do you want to start a rapid fire questionare?")
    inp=input("Do you want to start a Rapid Fire Questionnaire? (Yes/No): ").upper()
    if inp=="Y" or inp=="YES":
        for ques_no in range(1,6):      # Number Of Questions To Be Asked In Each Quiz
            r=random.randint(1,20)   # Random Questions From The List (Also, Set The Range)
    
            ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]     # Assigning Variables To All The Options
    
            quess=f"\nQuestion {str(ques_no)}: {ques[r][1]}"       # Displaying Question Along With Options
            print(quess)
            talk(quess)
    
            check_rapid_ans(answer="",r=r,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4)  # Calling Function To Check The Answer
    else:
        home()  

def check_rapid_ans(answer,r,ans1,ans2,ans3,ans4):

    answer=input("Answer: ").upper()
    if answer!=(ques[r][6]).upper():
        result = f"\nYour answer is incorrect.\nThe correct answer to this question is {ques[r][6]}." # If Answer Wrong
        print(result)
        talk(result)
    else:
        print("\nYour answer is correct!")    # If Answer Right
        talk("Your answer is correct!")

# ANSHUMAN'S FUNCTIONS

def facts():                         #Defining facts function
    with open("facts.txt") as fact_file:
        facts=fact_file.readlines()
        
        lis = ["Quite Amazing isn't it?","WOW!","Wow that's so cool!","Woah!","Haha nice","I love this one","This is actually crazy!"]
        fact = random.choice(facts)
        print("Your random space fact is : ", fact)
        talk(fact)
        var = random.choice(lis)
        talk(var)
        print(var)


def space_facts():
    while True:
        talk("Press enter to load your space fact or type anything to exit")
        answer = input("Press enter to load your space fact or type anything to exit: ")

        if answer == "":
            facts()
        else:
            home()
    

def home():
    print("\n Welcome to the home page! Choose a game mode to start with!")
    talk("Welcome to the home page! Choose a game mode to start with!")
    print("\n SPACE QUIZ \n RAPID FIRE \n SPACE FACTS")
    talk("Type in a game mode you want to play!")
    game_mode = input("Type in the game mode you want to play!: ")

    if game_mode.lower() == "space quiz":
        quiz()
    elif game_mode.lower() == "rapid fire":
        rapid_fire()
    elif game_mode.lower() == "space facts":
        space_facts()
    else:
        print("Please enter a valid game mode!")
        talk("Please enter a valid game mode!")
        exit()
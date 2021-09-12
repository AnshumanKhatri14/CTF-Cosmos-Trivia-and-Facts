# Trivia game using python and mysql connectivity (probably lol)

# Importing All The Used Modules

import csv
import random
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

# Files Needed To Be Read

ques_file=open("questions.csv")
read_ques_file=csv.reader(ques_file)
ques=[]         # 1-Q, 2-O1, 3-O2, 4-O3, 5-O4, 6-A
for x in read_ques_file:
    ques.append(x)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def quiz_again():      # Function To Start Another Quiz
    print("Do you want to take another quiz? (Yes/No): ")           # Ask If Want To Take One More Quiz Or Not
        
    talk("Do you want to take another quiz? (Yes or No)")
        
    inp=input().upper()
    if inp=="Y" or inp=="YES":
        for ques_no in range(1,6):      # Number Of Questions To Be Asked In Each Quiz
            r=random.randint(1,6)   # Random Questions From The List (Also, Set The Range)
            ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]     # Assigning Variables To All The Options

            print(f"\nQuestion {str(ques_no)}: {ques[r][1]}\n 1. {ques[r][2]}\n 2. {ques[r][3]}\n 3. {ques[r][4]}\n 4. {ques[r][5]}")    # Displaying Question Along With Options
            talk(f"\nQuestion {str(ques_no)}: {ques[r][1]}\nThe options are:\n first, {ques[r][2]}\n second, {ques[r][3]}\n third, {ques[r][4]}\n and fourth, {ques[r][5]}")
                        
            check_quiz_ans(answer="",r=r,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4)  # Calling Function To Check The Answer
    
    elif inp=="N" or inp == "NO":
        exit()  # FOR NOW Exit
    
    else:
        exit()  # FOR NOW Exit 

def check_quiz_ans(answer,r,ans1,ans2,ans3,ans4):    # Function To Take And Check The Answer
    print("\nEnter you answer (option 1, 2, 3, or 4): ")
    talk("Enter the correct option number (that is, one, two, three, or four)")
    
    answer=input()    # Input
    if (answer=="1" and ans1!=ques[r][6]) or (answer=="2" and ans2!=ques[r][6])\
        or (answer=="3" and ans3!=ques[r][6]) or (answer=="4" and ans4!=ques[r][6]):       # If Answer Wrong
        print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ques[r][6]}.")
        talk(f"\nYour answer is incorrect.\nThe correct answer to this question is; {ques[r][6]}.")
    
    else:
        print("\nYour answer is correct!")    # If Answer Right
        talk("Your answer is CORRECT!")

quiz_again()
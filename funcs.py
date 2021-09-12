# this is where all the funcs needed for main.py will be

talk("hello world")
ques_file=open("Questions\\question.txt")
opt1_file=open("Questions\\option_1.txt")
opt2_file=open("Questions\\option_2.txt")
opt3_file=open("Questions\\option_3.txt")
opt4_file=open("Questions\\option_4.txt")
ans_file=open("Questions\\answer.txt")

ques=ques_file.readlines()
opt1=opt1_file.readlines()
opt2=opt2_file.readlines()
opt3=opt3_file.readlines()
opt4=opt4_file.readlines()
ans=ans_file.readlines()

ques_file.close()
opt1_file.close()
opt2_file.close()
opt3_file.close()
opt4_file.close()
ans_file.close()

import random
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def quiz_again():      # Function To Start Another Quiz
        talk("Do you want to take another quiz?")
        inp=input("Do you want to take another quiz? (Yes/No): ").upper()   # Ask If Want To Take One More Quiz Or Not
        if inp=="Y" or inp=="YES":
                for ques_no in range(1,6):      # Number Of Questions To Be Asked In Each Quiz
                        r=random.randint(0,5)   # Random Questions From The Dicts (Also, Set The Range)
                        ans1,ans2,ans3,ans4=opt1[r],opt2[r],opt3[r],opt4[r]     # Assigning Variables To All The Options For Each Iteration
                        the_ques = print(f"\nQuestion {str(ques_no)}: {ques[r]} 1. {opt1[r]} 2. {opt2[r]} 3. {opt3[r]} 4. {opt4[r]}")    # Displaying Question Along With Options
                        talk(the_ques)
                        check_ans(answer="",r=r,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4)  # Calling Function To Check The Answer
        elif inp=="N" or inp == "NO":
                exit()  # FOR NOW Exit
        else:
                exit()  # FOR NOW Exit 

def check_ans(answer,r,ans1,ans2,ans3,ans4):    # Function To Take And Check The Answer
        talk("Enter your answer")
        answer=int(input("\nEnter you answer (option 1, 2, 3, or 4): "))    # Input
        if (answer==1 and ans1!=ans[r]) or (answer==2 and ans2!=ans[r])\
                 or (answer==3 and ans3!=ans[r]) or (answer==4 and ans4!=ans[r]):       # If Answer Wrong
                result = print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ans[r]}")
                talk(result)
        else:
                else_result = print("\nYour answer is correct!\n")    # If Answer Right
                talk(else_result)

quiz_again()
# YUGAM'S FUNCTIONS

def quiz_again():   # Function To Start Another Quiz
    
    talk("Do you want to take anther quiz?")
    inp=input("Do you want to take another quiz? (Yes/No): ").upper()   # Ask If Want To Take One More Quiz Or Not
    if inp=="Y" or inp=="YES":
        for ques_no in range(1,6):      # Number Of Questions To Be Asked In Each Quiz
            r=random.randint(1,6)   # Random Questions From The List (Also, Set The Range)
    
            ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]     # Assigning Variables To All The Options
    
            print(f"\nQuestion {str(ques_no)}: {ques[r][1]}\n 1. {ques[r][2]}\
            \n 2. {ques[r][3]}\n 3. {ques[r][4]}\n 4. {ques[r][5]}")    # Displaying Question Along With Options
    
            check_quiz_ans(answer="",r=r,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4)  # Calling Function To Check The Answer
    
    elif inp=="N" or inp == "NO":
        exit()  # FOR NOW Exit
    
    else:
        exit()  # FOR NOW Exit 

def check_quiz_ans(answer,r,ans1,ans2,ans3,ans4):    # Function To Take And Check The Answer
    
    talk("Enter your answer")
    answer=input("\nEnter you answer (option 1, 2, 3, or 4): ")    # Input
    if (answer=="1" and ans1!=ques[r][6]) or (answer=="2" and ans2!=ques[r][6])\
        or (answer=="3" and ans3!=ques[r][6]) or (answer=="4" and ans4!=ques[r][6]):       # If Answer Wrong
        result = print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ques[r][6]}.")
        talk(result)
    
    else:
        else_result = print("\nYour answer is correct!")    # If Answer Right
        talk(else_result)

def rapid_fire():
    talk("Do you want to take a rapid fire questionare?")
    inp=input("Do you want to start a Rapid Fire Questionaire? (Yes/No): ").upper()
    if inp=="Y" or inp=="YES":
        for ques_no in range(1,6):      # Number Of Questions To Be Asked In Each Quiz
            r=random.randint(1,6)   # Random Questions From The List (Also, Set The Range)
    
            ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]     # Assigning Variables To All The Options
    
            ques = print(f"\nQuestion {str(ques_no)}: {ques[r][1]}")    # Displaying Question Along With Options
            talk(ques)
    
            check_rapid_ans(answer="",r=r,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4)  # Calling Function To Check The Answer

def check_rapid_ans(answer,r,ans1,ans2,ans3,ans4):

    answer=input("Answer: ").upper()
    if answer!=(ques[r][6]).upper():
        result = print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ques[r][6]}.") # If Answer Wrong
        talk(result)
    else:
        print("\nYour answer is correct!")    # If Answer Right
        talk("Your answer is correct!")

# ANSHUMAN'S FUNCTIONS

def facts():                         #Defining facts function

    talk("Would you like to know a fun fact about space?")
    inpt=input("Would you like to know a fun fact about Space? (Yes/No): ").lower()       #Asking user would they like to know a space fact
    if inpt=="y" or inpt=="yes":                                                                       #When agreed
        with open("facts.txt") as fact_file:
            facts=fact_file.readlines()
            
            talk("your random space fact is")
            print("Your random space fact is : ", random.choice(facts))

    elif inpt=="n" or inpt=="no":
        talk("Hope you try it later")                                                                     #When denied
        print("Hope you try it later :)")
        exit()
    
    else:                                                                               #When input invalid
        talk("Your input is invalid, try again please")
        print("Your input is invalid, try again :)")
        exit()

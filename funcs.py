# this is where all the funcs needed for main.py will be

# YUGAM'S FUNCTIONS

def quiz_again():
    
    ques_file=open("questions.csv")
    read_ques_file=csv.reader(ques_file)
    ques=[]         # 1-Q, 2-O1, 3-O2, 4-O3, 5-O4, 6-A
    for x in read_ques_file:
        ques.append(x)      # Function To Start Another Quiz
    
    inp=input("Do you want to take another quiz? (Yes/No): ").upper()   # Ask If Want To Take One More Quiz Or Not
    if inp=="Y" or inp=="YES":
        for ques_no in range(1,6):      # Number Of Questions To Be Asked In Each Quiz
            r=random.randint(1,6)   # Random Questions From The List (Also, Set The Range)
    
            ans1,ans2,ans3,ans4=ques[r][2],ques[r][3],ques[r][4],ques[r][5]     # Assigning Variables To All The Options
    
            print(f"\nQuestion {str(ques_no)}: {ques[r][1]}\n 1. {ques[r][2]}\
            \n 2. {ques[r][3]}\n 3. {ques[r][4]}\n 4. {ques[r][5]}")    # Displaying Question Along With Options
    
            check_ans(answer="",r=r,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4)  # Calling Function To Check The Answer
    
    elif inp=="N" or inp == "NO":
        exit()  # FOR NOW Exit
    
    else:
        exit()  # FOR NOW Exit 

def check_ans(answer,r,ans1,ans2,ans3,ans4):    # Function To Take And Check The Answer
    
    answer=int(input("\nEnter you answer (option 1, 2, 3, or 4): "))    # Input
    if (answer==1 and ans1!=ques[r][6]) or (answer==2 and ans2!=ques[r][6])\
        or (answer==3 and ans3!=ques[r][6]) or (answer==4 and ans4!=ques[r][6]):       # If Answer Wrong
        print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ques[r][6]}.")
    
    else:
        print("\nYour answer is correct!")    # If Answer Right

def rapid_fire():
    inp=input("Do you want to start a Rapid Fire Questionaire? (Yes/No): ").upper()
    if inp=="Y" or inp=="YES":
        


# ANSHUMAN'S FUNCTIONS

def facts():                         #Defining facts function
    
    inpt=input("Would you like to know a fun fact about Space? (Yes/No): ").lower()       #Asking user would they like to know a space fact
    if inpt=="y" or inpt=="yes":                                                                       #When agreed
        with open("facts.txt") as fact_file:
            facts=fact_file.readlines()
            
            print("Your random space fact is : ", random.choice(facts))

    elif inpt=="n" or inpt=="no":                                                                     #When denied
        print("Hope you try it later :)")
        exit()
    
    else:                                                                               #When input invalid
        print("Your input is invalid, try again :)")
        exit()
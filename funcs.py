# this is where all the funcs needed for main.py will be

import random
import csv

ques_file=open("questions.csv","r")
read_ques_file=csv.reader(ques_file)
ques=[]         # 0-Q, 1-O1, 2-O2, 3-O3, 4-O4, 5-A
for x in read_ques_file:
        ques.append(x)

def quiz_again():      # Function To Start Another Quiz
        inp=input("Do you want to take another quiz? (Yes/No): ").upper()   # Ask If Want To Take One More Quiz Or Not
        if inp=="Y" or inp=="YES":
                for ques_no in range(1,6):      # Number Of Questions To Be Asked In Each Quiz
                        r=random.randint(0,5)   # Random Questions From The Dicts (Also, Set The Range)
                        ans1,ans2,ans3,ans4=ques[r][1],ques[r][2],ques[r][3],ques[r][4]     # Assigning Variables To All The Options For Each Iteration
                        print(f"\nQuestion {str(ques_no)}: {ques[r][0]}\n 1. {ques[r][1]}\
                                \n 2. {ques[r][2]}\n 3. {ques[r][3]}\n 4. {ques[r][4]}")    # Displaying Question Along With Options
                        check_ans(answer="",r=r,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4)  # Calling Function To Check The Answer
        elif inp=="N" or inp == "NO":
                exit()  # FOR NOW Exit
        else:
                exit()  # FOR NOW Exit 

def check_ans(answer,r,ans1,ans2,ans3,ans4):    # Function To Take And Check The Answer
        answer=int(input("\nEnter you answer (option 1, 2, 3, or 4): "))    # Input
        if (answer==1 and ans1!=ques[r][5]) or (answer==2 and ans2!=ques[r][5]) or (answer==3 and ans3!=ques[r][5]) or (answer==4 and ans4!=ques[r][5]):       # If Answer Wrong
                print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ques[r][5]}")
        else:
                print("\nYour answer is correct!\n")    # If Answer Right

quiz_again()
# this is where all the funcs needed for main.py will be

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

def quiz_again():      # Function To Start Another Quiz
        inp=input("Do you want to take another quiz? (Yes/No): ").upper()   # Ask If Want To Take One More Quiz Or Not
        if inp=="Y" and "YES":
                for ques_no in range(1,6):      # Number Of Questions To Be Asked In Each Quiz
                        r=random.randint(0,5)   # Random Questions From The Dicts (Also, Set The Range)
                        ans1,ans2,ans3,ans4=opt1[r],opt2[r],opt3[r],opt4[r]     # Assigning Variables To All The Options For Each Iteration
                        print(f"\nQuestion {str(ques_no)}: {ques[r]} 1. {opt1[r]} 2. {opt2[r]} 3. {opt3[r]} 4. {opt4[r]}")    # Displaying Question Along With Options
                        check_ans(answer="",r=r,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4)  # Calling Function To Check The Answer
        elif inp=="N" and "NO":
                exit()  # FOR NOW Exit
        else:
                exit()  # FOR NOW Exit 

def check_ans(answer,r,ans1,ans2,ans3,ans4):    # Function To Take And Check The Answer
        answer=int(input("\nEnter you answer (option 1, 2, 3, or 4): "))    # Input
        if (answer==1 and ans1!=ans[r]) or (answer==2 and ans2!=ans[r])\
                 or (answer==3 and ans3!=ans[r]) or (answer==4 and ans4!=ans[r]):       # If Answer Wrong
                print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ans[r]}")
        else:
                print("\nYour answer is correct!\n")    # If Answer Right

quiz_again()
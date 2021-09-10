# this is where all the funcs needed for main.py will be

#These ques ans are here to test the fucntions
ques={   1:"Which is the smallest planet within our solar system?"
        ,2:"Which is the second smallest planet within our solar system?"
        ,3:"The moon called Titan orbits which planet?"
        ,4:"Which is the brightest planet in the night’s sky?"
        ,5:"Which is the largest planet within our solar system?"
        ,6:"Uranus has only been visited by what spacecraft?"
}

opt1={   1:"Mercury"                            #C
        ,2:"Neptune"
        ,3:"Saturn"                             #C
        ,4:"Neptune"
        ,5:"Uranus"
        ,6:"Curiosity"
}

opt2={   1:"Uranus"
        ,2:"Mercury"
        ,3:"Jupiter"
        ,4:"Mercury"
        ,5:"Saturn"
        ,6:"The Voyager 2"                      #C
}

opt3={   1:"Mars"
        ,2:"Venus"
        ,3:"Venus"
        ,4:"Jupiter"
        ,5:"Jupiter"                            #C
        ,6:"Sputnik 1"
}

opt4={   1:"Venus"
        ,2:"Mars"                               #C
        ,3:"Mars"
        ,4:"Venus"                              #C
        ,5:"Neptune"
        ,6:"The Voyager 1"
}

ans={    1:opt1[1]
        ,2:opt4[2]
        ,3:opt1[3]
        ,4:opt4[4]
        ,5:opt3[5]
        ,6:opt2[6]
}

import random

def quiz_again():      # Function To Start Another Quiz
        inp=input("Do you want to take another quiz? (Yes/No): ").upper()   # Ask If Want To Take One More Quiz Or Not
        if inp=="Y" or "YES":
                for ques_no in range(1,6):      # Number Of Questions To Be Asked In Each Quiz
                        r=random.randint(1,6)   # Random Questions From The Dicts (Also, Set The Range)
                        ans1,ans2,ans3,ans4=opt1[r],opt2[r],opt3[r],opt4[r]     # Assigning Variables To All The Options For Each Iteration
                        print(f"\nQuestion {str(ques_no)}: {ques[r]}.\n1. {opt1[r]}\
                                \n2. {opt2[r]}\n3. {opt3[r]}\n4. {opt4[r]}")    # Displaying Question Along With Options
                        check_ans(answer="",r=r,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4)  # Calling Function To Check The Answer
        else:
                exit()  # FOR NOW Exit

def check_ans(answer,r,ans1,ans2,ans3,ans4):    # Function To Take And Check The Answer
        answer=input("\nEnter you answer (option 1, 2, 3, or 4): ")     # Input
        if answer!=None:        # Checking The Answer
                if answer=="1":         # If Selected 1
                        if ans1==ans[r]:
                                print("\nYour answer is correct!\n")
                        else:
                                print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ans[r]}.\n")
                elif answer=="2":       # If Selected 2
                        if ans2==ans[r]:
                                print("\nYour answer is correct!\n")
                        else:
                                print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ans[r]}.\n")
                elif answer=="3":       # If Selected 3
                        if ans3==ans[r]:
                                print("\nYour answer is correct!\n")
                        else:
                                print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ans[r]}.\n")
                elif answer=="4":       # If Selected 4
                        if ans4==ans[r]:
                                print("\nYour answer is correct!\n")
                        else:
                                print(f"\nYour answer is incorrect.\nThe correct answer to this question is {ans[r]}.\n")
        else:
                print("Please check your answer.")

quiz_again()
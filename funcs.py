# this is where all the functions will be that are needed for main.py

# function to print all the questions and get answer

def print_ques():
        with open("Questions/question.txt") as f:
                ques = f.readlines()
                for ques_no in range(6):
                        print(f"Q{int(ques_no)+1}: {ques[ques_no]}")


print_ques()

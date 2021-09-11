import random
def facts():                         #Defining facts function
    inpt=input("Would you like to know a fun fact about Space? (y/n) : ").lower()                       #Asking user would they like to know a space fact
    if inpt=="y":                                                                               #When agreed
        import random 
        with open("babatunde.txt","r") as f:
            facts=f.readlines()
            print("Your random space fact is : " )
            print(random.choice(facts))
    elif inpt=="n":                                                                             #When denied
        print("Hope you try it later :)")
        exit()
    else:                                                                                       #When input invalid
        print("Your input is invalid, try again :)")
        exit()

facts()                                                                                         #Calling function


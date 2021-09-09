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

def random_ques():
    inp=input("Do you want to take another quiz? (Yes/No)").upper()
    if inp=="Y" or "YES":
        for i in range(1,6):
            r=random.randint(1,6)
            print(ques[r])
            user_ans()

def user_ans():
    answer=input("Enter you answer (option 1, 2, 3, or 4): ")
    if answer==ans[]
import time
from PIL import Image, ImageFilter
def main():
    print ("Welcome to my Museum!")
    time.sleep(1)
    print ("Here we have various works of art on display created by yours truly.")
    time.sleep(1)
    print ("Where would you like to explore?")
    time.sleep(1)
    Wing_Choice = input ("Personal, School, or Map? ")
    if Wing_Choice == ("Personal"):
        PersonalWing()
    elif Wing_Choice == ("School"):
        SchoolWing()

def PersonalWing():
    time.sleep(1)
    print ("Welcome to the North Wing of the museum!")
    time.sleep(1)
    print ("This is where all the 3D models done in my spare time reside.")
    time.sleep(1)
    print ("A lot of our pieces here were birthday gifts, but several were done just as great additions to the portfolio.")
    time.sleep(1)
    PersonalWingQuestions()
def PersonalWingQuestions():
    print ("Would you like to take a look at our pieces here?")
    time.sleep(1)
    PersonalWingChoice = input ("Y or N? ")
    if PersonalWingChoice == ("Y"):
        PersonalWingPieces()
    elif PersonalWingChoice == ("N"):
        time.sleep(1)
        print ("Would you like to go to a different wing?")
        ChangeWingPersonal = input ("Y or N? ")
        
        if ChangeWingPersonal ==("Y"):
            main()
        else:
            PersonalWingQuestions()
    else:
        print ("Sorry, I didn't catch that, let me repeat myself.")
        PersonalWingQuestions()

def PersonalWingPieces():
    print ("What piece would you like to take a look at?")
    PersonalWingPieceChoice = input ("Rylee, Campbell, Andrea, Lidya, or more ")

def SchoolWing():
    print ("Welcome to the West Wing of the museum!")
    print ("This is where all the 3D models done for class projects reside.")

if __name__ == "__main__":
    main()
import time
from PIL import Image, ImageFilter, ImageShow
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
    print ("Birthday gifts are where my best work in my free time has been done, so all four of the pieces in this hall are birthday gifts I've made for friends. ")
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
    PersonalWingPieceChoice = input ("Rylee, Campbell, Andrea, Lidya, or Leave? ")
    if PersonalWingPieceChoice == ("Campbell"):
        with Image.open ("Campbell Render.jpg") as img:
            img.show()
            img.close()
        LearnCampbell()
    elif PersonalWingPieceChoice == ("Rylee"):
        with Image.open ("Campbell Render.jpg") as img:
            img.show
    elif PersonalWingPieceChoice == ("Lidya"):
        with Image.open ("Lidya_Wideshot_Litup.jpg") as img:
            img.show()
            img.close()
            LearnLidya()
    elif PersonalWingPieceChoice == ("Andrea"):
        with Image.open ("AndreaGift_CloseUp.jpg") as img:
            img.show()
            img.close()
            LearnAndrea()
    elif PersonalWingPieceChoice == ("Leave"):
        main()
    else:
        print ("Sorry, I didn't catch that, let me repeat myself.")
        PersonalWingPieces()

def LearnCampbell():
    print ("Would you like to learn more?")
    LearnMoreCampbell = input ("Y or N? ")
    if LearnMoreCampbell == ("Y"):
        print ("I made this piece for my friend Campbell's birthday back in 2024.")
        print ("I wanted to capture all her favorite interests in this model.")
        print ("I implemented her love of reading via the book model.")
        print ("Meanwhile I implemented her love for Marvel in the floating set pieces such as the lightsaber and horned crown.")
        print ("Then I implemented her love for games with the meeple and the die.")
        print ("Finally I implemented her favorite color combo in the name model.")
        PersonalWingPieces()
    elif LearnMoreCampbell == ("N"):
        PersonalWingPieces()
    else:
        print ("Sorry, I didn't catch that, let me repeat myself.")
        LearnCampbell()
def LearnLidya():
    print ("Would you like to learn more?")
    LearnMoreLidya = input ("Y or N? ")
    if LearnMoreLidya == ("Y"):
        print ("I made this piece for my friend Lidya's birthday back in 2024.")
        print ("I wanted to capture all her favorite interests in this model.")
        print ("I implemented her love of movies via the camera and projector screen.")
        print ("Meanwhile I implemented her love cowboys via the cactus and cowboy hat on the cactus, lizard, and desert scenery.")
        print ("Then I implemented her love for reptiles with the lizard")
        print ("Finally I implemented her favorite color combo in the name model.")
        PersonalWingPieces()
    elif LearnMoreLidya == ("N"):
        PersonalWingPieces()
    else:
        print ("Sorry, I didn't catch that, let me repeat myself.")
        LearnLidya()


def LearnAndrea():
    print ("Would you like to learn more?")
    LearnMoreAndrea = input ("Y or N? ")
    if LearnMoreAndrea == ("Y"):
        print ("I made this piece for my friend Andrea's birthday back in 2024.")
        print ("I wanted to capture all her favorite interests in this model.")
        print ("The main thing I implemented here was her love of cats as it was the main bit of info I had going into it.")
        print ("But I also implemented her favorite color combo in the name model.")
        PersonalWingPieces()
    elif LearnMoreAndrea == ("N"):
        PersonalWingPieces()
    else:
        print ("Sorry, I didn't catch that, let me repeat myself.")
        LearnLidya()

def SchoolWing():
    print ("Welcome to the West Wing of the museum!")
    print ("This is where all the 3D models done for class projects reside.")
    print ("They may be class projects, but that doesn't mean I didn't put my heart and soul into")
    SchoolWingQuestions()

def SchoolWingQuestions():
    print ("Would you like to take a look at our pieces here?")
    time.sleep(1)
    SchoolWingChoice = input ("Y or N? ")
    if SchoolWingChoice == ("Y"):
        SchoolWingPieces()
    elif SchoolWingChoice == ("N"):
        time.sleep(1)
        print ("Would you like to go to a different wing?")
        ChangeWingPersonal = input ("Y or N? ")
        
        if ChangeWingPersonal ==("Y"):
            main()
        else:
            SchoolWingQuestions()
    else:
        print ("Sorry, I didn't catch that, let me repeat myself.")
        SchoolWingQuestions()   


def SchoolWingPieces():
    print ("What piece would you like to take a look at?")
    SchoolWingPieceChoice = input ("Rylee, Campbell, Andrea, Lidya, or more ")
    if SchoolWingPieceChoice == ("campbell"):
        DisplayCampbellArt()   
if __name__ == "__main__":
    main()
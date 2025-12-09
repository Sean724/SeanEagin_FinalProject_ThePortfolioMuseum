import time
from PIL import Image, ImageFilter, ImageShow
def main():
    print ("Welcome to my Museum!")
    time.sleep(1.5)
    print ("Here we have various works of art on display created by yours truly.")
    time.sleep(1.5)
    Wings()

def Wings():
    print ("Where would you like to explore?")
    time.sleep(1.5)
    Wing_Choice = input ("Personal, School, 2D, or Leave? ")
    Wing_Choice = Wing_Choice.lower()
    if Wing_Choice == ("personal"):
        PersonalWing()
    elif Wing_Choice == ("school"):
        SchoolWing()
    elif Wing_Choice == ("2d"):
        finalwing()
    elif Wing_Choice == ("leave"):
        SystemExit("Thank you for coming!")
    else:
        Wings()

def PersonalWing():
    time.sleep(1.5)
    print ("Welcome to the East Wing of the museum!")
    time.sleep(1.5)
    print ("This is where all the 3D models done in my spare time reside.")
    time.sleep(1.5)
    print ("Birthday gifts are where my best work in my free time has been done, so all four of the pieces in this hall are birthday gifts I've made for friends. ")
    time.sleep(1.5)
    PersonalWingQuestions()
def PersonalWingQuestions():
    print ("Would you like to take a look at our pieces here?")
    time.sleep(1.5)
    PersonalWingChoice = input ("Y or N? ")
    PersonalWingChoice = PersonalWingChoice.lower()
    if PersonalWingChoice == ("y"):
        PersonalWingPieces()
    elif PersonalWingChoice == ("n"):
        time.sleep(1.5)
        print ("Would you like to go to a different wing?")
        ChangeWingPersonal = input ("Y or N? ")
        ChangeWingPersonal = ChangeWingPersonal.lower()
        if ChangeWingPersonal ==("y"):
            Wings()
        else:
            PersonalWingQuestions()
    else:
        time.sleep(1.5)
        print ("Sorry, I didn't catch that, let me repeat myself.")
        PersonalWingQuestions()

def PersonalWingPieces():
    time.sleep(1.5)
    print ("What piece would you like to take a look at?")
    time.sleep(1.5)
    PersonalWingPieceChoice = input ("Rylee, Campbell, Andrea, Lidya, or Leave? ")
    PersonalWingPieceChoice = PersonalWingPieceChoice.lower()
    if PersonalWingPieceChoice == ("campbell"):
        with Image.open ("Campbell Render.jpg") as img:
            img.show()
            img.close()
        LearnCampbell()
    elif PersonalWingPieceChoice == ("rylee"):
        with Image.open ("Campbell Render.jpg") as img:
            img.show()
            img.close()
    elif PersonalWingPieceChoice == ("lidya"):
        with Image.open ("Lidya_Wideshot_Litup.jpg") as img:
            img.show()
            img.close()
            LearnLidya()
    elif PersonalWingPieceChoice == ("andrea"):
        with Image.open ("AndreaGift_CloseUp.jpg") as img:
            img.show()
            img.close()
            LearnAndrea()
    elif PersonalWingPieceChoice == ("leave"):
        Wings()
    else:
        print ("Sorry, I didn't catch that, let me repeat myself.")
        PersonalWingPieces()

def LearnCampbell():
    time.sleep(1.5)
    print ("Would you like to learn more?")
    time.sleep(1.5)
    LearnMoreCampbell = input ("Y or N? ")
    LearnMoreCampbell = LearnMoreCampbell.lower()
    if LearnMoreCampbell == ("y"):
        time.sleep(1.5)
        print ("I made this piece for my friend Campbell's birthday back in 2024.")
        time.sleep(1.5)
        print ("I wanted to capture all her favorite interests in this model.")
        time.sleep(1.5)
        print ("I implemented her love of reading via the book model.")
        time.sleep(1.5)
        print ("Meanwhile I implemented her love for Marvel in the floating set pieces such as the lightsaber and horned crown.")
        time.sleep(1.5)
        print ("Then I implemented her love for games with the meeple and the die.")
        time.sleep(1.5)
        print ("Finally I implemented her favorite color combo in the name model.")
        PersonalWingPieces()
    elif LearnMoreCampbell == ("n"):
        PersonalWingPieces()
    else:
        time.sleep(1.5)
        print ("Sorry, I didn't catch that, let me repeat myself.")
        LearnCampbell()
def LearnLidya():
    time.sleep(1.5)
    print ("Would you like to learn more?")
    time.sleep(1.5)
    LearnMoreLidya = input ("Y or N? ")
    LearnMoreLidya = LearnMoreLidya.lower()
    if LearnMoreLidya == ("y"):
        time.sleep(1.5)
        print ("I made this piece for my friend Lidya's birthday back in 2024.")
        time.sleep(1.5)
        print ("I wanted to capture all her favorite interests in this model.")
        time.sleep(1.5)
        print ("I implemented her love of movies via the camera and projector screen.")
        time.sleep(1.5)
        print ("Meanwhile I implemented her love cowboys via the cactus and cowboy hat on the cactus, lizard, and desert scenery.")
        time.sleep(1.5)
        print ("Then I implemented her love for reptiles with the lizard")
        time.sleep(1.5)
        print ("Finally I implemented her favorite color combo in the name model.")
        PersonalWingPieces()
    elif LearnMoreLidya == ("n"):
        PersonalWingPieces()
    else:
        time.sleep(1.5)
        print ("Sorry, I didn't catch that, let me repeat myself.")
        LearnLidya()

def LearnRylee():
    print ("Would you like to learn more?")
    LearnMoreRylee = input ("Y or N? ")
    LearnMoreRylee = LearnMoreRylee.lower()
    if LearnMoreRylee == ("y"):
        print ("I made this piece for my friend Andrea's birthday back in 2024.")
        print ("I wanted to capture all her favorite interests in this model.")
        print ("The main thing I implemented here was her love of cats as it was the main bit of info I had going into it.")
        print ("But I also implemented her favorite color combo in the name model.")
        PersonalWingPieces()
    elif LearnMoreRylee == ("n"):
        PersonalWingPieces()
    else:
        print ("Sorry, I didn't catch that, let me repeat myself.")
        LearnRylee()

def LearnAndrea():
    time.sleep(1.5)
    print ("Would you like to learn more?")
    time.sleep(1.5)
    LearnMoreAndrea = input ("Y or N? ")
    LearnMoreAndrea = LearnMoreAndrea.lower()
    if LearnMoreAndrea == ("y"):
        time.sleep(1.5)
        print ("I made this piece for my friend Andrea's birthday back in 2024.")
        time.sleep(1.5)
        print ("I wanted to capture all her favorite interests in this model.")
        time.sleep(1.5)
        print ("The main thing I implemented here was her love of cats as it was the main bit of info I had going into it.")
        time.sleep(1.5)
        print ("But I also implemented her favorite color combo in the name model.")
        PersonalWingPieces()
    elif LearnMoreAndrea == ("n"):
        PersonalWingPieces()
    else:
        time.sleep(1.5)
        print ("Sorry, I didn't catch that, let me repeat myself.")
        LearnAndrea()

def finalwing():
    time.sleep(1.5)
    print ("Welcome to the North Wing of the museum!")
    time.sleep(1.5)
    print ("This is where all the non 3D Model artwork resides")
    time.sleep(1.5)
    print ("They may not be my strength area, but I've put in a lot of effort all the same.")
    FinalWingQuestions()

def FinalWingQuestions():
    time.sleep(1.5)
    print ("Would you like to take a look at our pieces here?")
    time.sleep(1.5)
    FinalWingChoice = input ("Y or N? ")
    FinalWingChoice = FinalWingChoice.lower()
    if FinalWingChoice == ("y"):
        FinalWingPieces()
    elif FinalWingChoice == ("n"):
        time.sleep(1.5)
        print ("Would you like to go to a different wing?")
        ChangeWingPersonal = input ("Y or N? ")
        
        if ChangeWingPersonal ==("Y"):
            time.sleep(1.5)
            Wings()
        else:
            FinalWingQuestions()
    else:
        time.sleep(1.5)
        print ("Sorry, I didn't catch that, let me repeat myself.")
        FinalWingQuestions()


def FinalWingPieces():
    time.sleep(1.5)
    print ("What piece would you like to take a look at?")
    time.sleep(1.5)
    FinalWingPieceChoice = input ("Portrait, Mask, Collage, or Leave? ")
    FinalWingPieceChoice = FinalWingPieceChoice.lower()
    if FinalWingPieceChoice == ("portrait"):
        with Image.open ("AbstractSelfPortrait.jpg") as img:
            img.show()
            img.close()
        LearnPortrait()
    elif FinalWingPieceChoice == ("mask"):
        with Image.open ("ColorInCulture_Finished.jpg") as img:
            img.show()
            img.close()
            LearnMask()
    elif FinalWingPieceChoice == ("Collage"):
        with Image.open ("photocollage-eagin-sean-final.jpg") as img:
            img.show()
            img.close()
            LearnCollage()
    elif FinalWingPieceChoice == ("leave"):
        time.sleep(1.5)
        main()
    else:
        time.sleep(1.5)
        print ("Sorry, I didn't catch that, let me repeat myself.")
        FinalWingPieces()

def LearnPortrait():
    time.sleep(1.5)
    print ("Would you like to learn more?")
    time.sleep(1.5)
    LearnMorePortrait = input ("Y or N? ")
    LearnMorePortrait = LearnMorePortrait.lower()
    if LearnMorePortrait == ("y"):
        time.sleep(1.5)
        print ("I made this piece for a class assignment back in 2023.")
        time.sleep(1.5)
        print ("This is my favorite non modeled piece I've ever done.")
        time.sleep(1.5)
        print ("The combination of colors when put together with the pattern textures I used is really visually appealing to me.")
        time.sleep(1.5)
        print ("I also loved how well I feel like I captured myself.")
        time.sleep(1.5)
        print ("Then finally, I really love the gradient in the background as gradients are something I struggle heavily with.")
        FinalWingPieces()
    elif LearnMorePortrait == ("n"):
        FinalWingPieces()
    else:
        time.sleep(1.5)
        print ("Sorry, I didn't catch that, let me repeat myself.")
        LearnPortrait()

def LearnMask():
    time.sleep(1.5)
    print ("Would you like to learn more?")
    time.sleep(1.5)
    LearnMoreMask = input ("Y or N? ")
    LearnMoreMask = LearnMoreMask.lower()
    if LearnMoreMask == ("y"):
        time.sleep(1.5)
        print ("I made this piece for a class assignment back in 2024.")
        time.sleep(1.5)
        print ("This was created in an effort to capture the vibe of the Day of the Dead celebrations in Mexico.")
        time.sleep(1.5)
        print ("I aimed to accomplish this with the mask, but also vibrant, yet fall feeling colors.")
        time.sleep(1.5)
        print ("In the end I'm really happy with how it came out, most of all the flowers.")
        FinalWingPieces()
    elif LearnMoreMask == ("n"):
        FinalWingPieces()
    else:
        time.sleep(1.5)
        print ("Sorry, I didn't catch that, let me repeat myself.")
        LearnMask()

def LearnCollage():
    time.sleep(1.5)
    print ("Would you like to learn more?")
    time.sleep(1.5)
    LearnMoreCollage = input ("Y or N? ")
    LearnMoreCollage = LearnMoreCollage.lower()
    if LearnMoreCollage == ("y"):
        time.sleep(1.5)
        print ("I made this piece for a class assignment back in 2024.")
        time.sleep(1.5)
        print ("This piece was created in order to capture my personality in the best way possible.")
        time.sleep(1.5)
        print ("First off, I'm a big fan or magic and medieval fantasy, so I knew I wanted to do something with that.")
        time.sleep(1.5)
        print ("Then there's the way in which I implemented my generally kind and caring nature through the display of nature based magic, also animals like butterflies and the dog.")
        time.sleep(1.5)
        print ("All in all I'm really happy with how it came out in the end, definitely a success.")
        FinalWingPieces()
    elif LearnMoreCollage == ("n"):
        FinalWingPieces()
    else:
        time.sleep(1.5)
        print ("Sorry, I didn't catch that, let me repeat myself.")
        LearnPortrait()

def SchoolWing():
    time.sleep(1.5)
    print ("Welcome to the West Wing of the museum!")
    time.sleep(1.5)
    print ("This is where all the 3D models done for class projects reside.")
    time.sleep(1.5)
    print ("They may be class projects, but that doesn't mean I didn't put my heart and soul into")
    SchoolWingQuestions()

def SchoolWingQuestions():
    time.sleep(1.5)
    print ("Would you like to take a look at our pieces here?")
    time.sleep(1.5)
    SchoolWingChoice = input ("Y or N? ")
    if SchoolWingChoice == ("Y"):
        SchoolWingPieces()
    elif SchoolWingChoice == ("N"):
        time.sleep(1.5)
        print ("Would you like to go to a different wing?")
        ChangeWingPersonal = input ("Y or N? ")
        if ChangeWingPersonal ==("Y"):
            main()
        else:
            SchoolWingQuestions()
    else:
        time.sleep(1.5)
        print ("Sorry, I didn't catch that, let me repeat myself.")
        SchoolWingQuestions()   

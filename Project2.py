###HISTORY CLASS###
#You just arrived to school. You have to prepare before history class (or procrastrinate and fail.) The global variable used is learninglevel. If it is above 5, you pass the test. If it is below 5, you fail the test.                                               

########
#import modules
#######

########
#define functions
#######
def start():
    print("Welcome! You have to go to history class but did not study. The more you procrastinate and do fun things, the lower your learning level. If your learning level is high enough, you will pass the test. Every time you go out and back into the library, your learning level increases by 2.5")
    townhall()

def townhall():
    global learninglevel
    learninglevel=learninglevel+0
    print("\nYou are in the townhall")
    move = input("\nWhere would you like to go? Say one of these choices:\nlibrary\ncafeteria\ngym\nhistory class\n")
    if move.lower() == "library":
        library()
    elif move.lower() == "cafeteria":
        cafeteria()
    elif move.lower() == "gym":
        gym()
    elif move.lower() == "history class":
        history_class()
    
    else:
        #TODO: what should happen if they type something else?
        print("Sorry, this is not an available option. Please choose another.\n")
        townhall()

def library():
    global learninglevel
    learninglevel = learninglevel+2.5
    print("\nYou are in the library. Your knowledge level has increased by 2.5! You need to take a rest before you continue studying. You go back to the townhall")
    townhall()

def cafeteria():
    print("\nYou decide that you are hungry and go to the cafeteria.\nAfter you finish eating you realize it is time to go back.")
    townhall()

def gym():
    global learninglevel
    learninglevel = learninglevel + 2
    print("\nYou met a friend when you were shooting hoops. He told you the answers to some of the quesitons. Your learning level has increased by 2")
    print("You get tired and go back to the townhall.\n")
    townhall()

def history_class():
    global learninglevel
    print("\nIt is finally time! You take the test")
    if learninglevel>5:
        print("You passed! Congratulations!")
    elif learninglevel<5:
        print("You failed! Should've went to the library more.")


########
#main
#######
#TODO: Add some global variables
learninglevel=0
start()
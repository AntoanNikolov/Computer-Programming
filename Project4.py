from cmu_graphics import *
#This is a simple game. The user input influences the ending.
input1=input("You wake up in the middle of a forrest. You hear the distant hums of cars in the distance. That's weird, perhaps you drank too much yesterday. \nYou stumble upon three houses. One is blue, one is red, and the other one is green. Which one would you like to investigate? ")
if input1=="blue":
    print("You enter the house. A figure runs towards you. Everything turns to black. \nYou Died.")
elif input1=="red":
    print("Congratulations! You picked the right house. You see a portal that leads directly to your home.")
elif input1=="green":
    input2=input("As you enter, you sense a weird smell. You begin to feel drowsy. Would you like to fall asleep?")
    if input2=="yes":
        print("You fall asleep and die.")
    if input2=="no":
        print("You continue to walk but the poisonous scent kills you.")
int(input("Thanks for playing! Please rate this game on a scale from 1-10 " ))
print("Thanks for the Score!")
Rect(125,80,30,80)
Rect(245,80,30,80)
Rect(50,200,25,75)
Rect(325,200,25,75)
Rect(75,275,250,40)

cmu_graphics.run()
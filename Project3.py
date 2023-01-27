import random

rolls = 0 #how many times we rolled the dice
getasix = 0 #how many times we got a six

while getasix < 1000: 
    number = random.randint(1, 6) #each time we roll we get a different num
    rolls += 1
    if number == 6:
        getasix += 1 #store the amount of times we got a six in getasix

average_rolls = rolls / 1000
print("It took an average of", average_rolls, "rolls to get a 6 for 1000 trials")

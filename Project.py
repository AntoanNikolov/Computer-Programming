#Name: Antoan
#This code takes a side of a square, finds its area, and draws it.
import turtle
square=turtle.Turtle() #creates a turtle and assings it to a variable called "square."
side_of_sq=int(input("How long is the side of the square?")) #The user gives the length of their square
print("The area of the square is:")
print(side_of_sq*side_of_sq) #this calculates the area of the square
#The next lines draw the square using the side, given by the user. The turtle draws a line in each direction with a length of side_of_sq and always takes a 90 degree turn.

square.forward(side_of_sq)
square.left(90)

square.forward(side_of_sq)
square.left(90)

square.forward(side_of_sq)
square.left(90)

square.forward(side_of_sq)
square.left(90)

print("Enjoy your beautiful square!")

turtle.done() #executes the drawing
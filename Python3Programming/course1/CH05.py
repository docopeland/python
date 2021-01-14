# Write a program that prints We like Python's turtles! 10 times.
for _ in range(10):
    print("We like Python's turtles!")

# Use for loops to make a turtle draw regular polygons (regular means all sides the same lengths, all angles the same)
import turtle
back = turtle.Screen()
lil = turtle.Turtle()
shape = input("What shape should lil turtle draw?")
# triangle
if shape == "triangle":
    for _ in range(3):
        lil.forward(100)
        lil.right(120)
if shape == "square":
    for _ in range(4):
        lil.forward(100)
        lil.right(90)
if shape == "hexagon":
    for _ in range(6):
        lil.forward(100)
        lil.right(60)
if shape == "octagon":
    for _ in range(8):
        lil.forward(50)
        lil.right(45)

# Create a turtle and assign it to a variable. When you print its type, what do you get?
turt = turtle.Turtle()
print(type(turt))
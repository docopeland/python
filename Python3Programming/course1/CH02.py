# Challenge: Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently
# 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general
# version of the above problem. Ask the user for the time now (in hours), and then ask for the number of hours to wait
# for the alarm. Your program should output what the time will be on the clock when the alarm goes off.
timeNow = input("What time is it now?")
timeThen = (int(timeNow) + 50) % 24
print(timeThen)

# It is possible to name the days 0 thru 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful
# holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a
# Saturday (day 6). Write a general version of the program which asks for the starting day number, and the length of
# your stay, and it will tell you the number of day of the week you will return on.
dayLeave = input("What day did you leave?")
lenofStay = input("How long was your stay?")
dayReturn = (int(dayLeave) + int(lenofStay)) % 7
print(dayReturn)

# Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, and assign
# to r the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, t, that the money
# will be compounded for. Calculate and print the final amount after t years.
P = 10000
n = 12
r = 0.08
t = input("Number of years?")
A = P*(1 + (r/n))**(n*int(t))
print(A)

# Write a program that will compute the area of a circle. Prompt the user to enter the radius and save it to a variable
# called radius. Print a nice message back to the user with the answer.
pi = 3.14
radius = input("Radius of circle?")
area = pi * int(radius)**2
print(area)

# Challenge: Write a program that will compute the area of a rectangle. Prompt the user to enter the width and height
# of the rectangle and store the values in variables called width and height. Print a nice message with the answer..
width = input("width of rectangle ")
height = input("height of rectangle ")
area = int(height) * int(width)
print(area)

# Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number
# of gallons used. Print a nice message with the answer.
miles = input("miles driven")
gallons = input("gallons used")
mpg = int(miles) / int(gallons)
print(mpg)

# Challenge: Write a program that will convert degrees celsius to degrees fahrenheit.
degC = input("degrees in Celsius")
degF = int(degC) * (9 / 5) + 32
print(degF)

# Ask the user for the temperature in Fahrenheit and store it in a variable call deg_f. Calculate the equivalent
# temperature in degrees Celsius and store it in def_c. Output a message to the user giving the temperature in Celsius.
deg_f = input("degrees in Farenheit")
deg_c = (int(deg_f) - 32) * (5 / 9)
print(deg_c)
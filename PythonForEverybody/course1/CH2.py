# Assignment 2.2
# 2.2 Write a program that uses input to prompt a user for their name and then welcomes them. Note that input will pop
# up a dialog box.
name = input("Enter your name ")
print("Hello " + name)

# Assignment 2.3
# 2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours
# and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string
# and float() to convert the string to a number. Do not worry about error checking or bad user data.
hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
print("Pay:", float(hrs)*float(rate))

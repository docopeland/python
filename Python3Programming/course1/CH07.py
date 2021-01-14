# In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings are Jack, Kack, Lack, Mack, Nack,
# Ouack, Pack, and Quack. This loop tries to output these names in order.
prefixes = "JKLMNOPQ"
suffix = "ack"
for p in prefixes:
    if (p == "O") or (p == "Q"):
        suffix = "uack"
    print(p + suffix)

# Get the user to enter some text and print it out in reverse order.
text = input("tell me a word")
newText = ""
for let in range(len(text),0,-1):
    newText += text[let-1]
print(newText)

# Write a program that uses a for loop to print
# One of the months of the year is January
# One of the months of the year is February
# One of the months of the year is March, etc.
months = ["January","February","March","April","May","June","July","September","October","November","December"]
for i in months:
    print("One of the months of the year is " + i)

# Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20. Write a loop that prints each number and its
# square on a new line.
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in numbers:
    print("The square of",i,"is",i*i)


# assignment 7.1
# Write a program that prompts for a file name, then opens that file and reads through the file, and print the
# contents of the file in upper case.

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    print(line.upper().rstrip())

# assignment 7.2
# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of
# the form: X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those
# values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

fname = input("Enter file name: ")
fOpen = open(fname)
count = 0
values = 0
for line in fOpen:
    if line.startswith("X-DSPAM-Confidence"):
        count = count + 1
        values = values + float(line[line.find(" "):].strip())
    else:
        continue
print("Average spam confidence:", values/count)

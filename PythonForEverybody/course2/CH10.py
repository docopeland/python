# assignment 10.2
# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
# the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
# second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour.

fName = input("Enter file: ")
if len(fName) < 1:
    fName = "mbox-short.txt"
fHandle = open(fName)
hours = dict()
for line in fHandle:
    if line.strip().startswith("From "):
        hours[line.split()[5][:2]] = hours.get(line.split()[5][:2],0) + 1
    else:
        continue
for k,v in sorted(hours.items()):
    print(k,v)

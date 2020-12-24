# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers
# in the file and compute the sum of the numbers.
# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a
# regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

import re
fName = input("Enter file name: ")
fHandle = open(fName)
nums = list()
for line in fHandle:
    if re.search('[0-9]+',line.rstrip()):
        nums.append(re.findall('[0-9]+',line.rstrip()))
final = [int(val) for sublist in nums for val in sublist]
print(sum(final))

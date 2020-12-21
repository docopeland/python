# assignment 6.5
# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475"
# finding the first string occuran e of a space
spaceNo = text.find(" ")
# getting the substring from space to end of string
new1 = text[spaceNo:]
# stripping the string of all whitespaces
new2 = new1.strip()
# making it a float
newText = float(new2)
print(newText)

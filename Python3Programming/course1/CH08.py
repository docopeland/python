# rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month
# (in inches) with every month separated by a comma. Write code to compute the number of months that have more than
# 3 inches of rainfall. Store the result in the variable num_rainy_months. In other words, count the number of items
# with values > 3.0.
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rainfall_mi = rainfall_mi.split(", ")
num_rainy_months = 0
for rain in rainfall_mi:
    if float(rain) > 3:
        num_rainy_months += 1
print("the number of rainy months are",num_rainy_months)

# The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same
# letter, including one-letter words. Store the result in the variable same_letter_count.
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
sentence = sentence.split()
same_letter_count = 0
for words in sentence:
    if words[0] == words[-1]:
        same_letter_count += 1
print("the number of words that start and end with the same letter are",same_letter_count)

# Write code to count the number of strings in list items that have the character w in it. Assign that number to the
# variable acc_num.
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for item in items:
    if "w" in item:
        acc_num += 1
print("the number of words that have the letter w in it are",acc_num)

# Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the
# variable num_a_or_e.
sentence = "python is a high level general purpose programming language that can be applied to many different classes " \
           "of problems."
sentence = sentence.split()
num_a_or_e = 0
for words in sentence:
    if "a" in words or "e" in words:
        num_a_or_e += 1
print("the number of words in the sentence that contain either 'a' or 'e' are",num_a_or_e)

# Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels.
# For this problem, vowels are only a, e, i, o, and u. Hint: use the in operator with vowels.
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels = 0
for char in s:
    if char in vowels:
        num_vowels += 1
print("the number of vowels in this sentence are",num_vowels)

# Create one conditional so that if “Friendly” is in w, then “Friendly is here!” should be assigned to the variable wrd.
# If it’s not, check if “Friend” is in w. If so, the string “Friend is here!” should be assigned to the variable wrd,
# otherwise “No variation of friend is in here.” should be assigned to the variable wrd. (Also consider: does the order
# of your conditional statements matter for this problem? Why?)
w = "Friendship is a wonderful human experience!"
if "Friendly" in w:
    wrd = "Friendly is here!"
elif "Friend" in w:
    wrd = "Friend is here!"
else:
    wrd = "No variation of friend is in here."
print(wrd)

# Write code so that if "STATS 250" is in the list schedule, then the string "You could be in Information Science!" is
# assigned to the variable resp. Otherwise, the string "That's too bad." should be assigned to the variable resp.
schedule = ["SI 106", "STATS 250", "SI 110", "ENGLISH 124/125"]
if "SI 106" in schedule:
    resp = "You could be in Information Science!"
else:
    resp = "That's too bad."
print(resp)

# Create the variable z whose value is 30. Write code to see if z is greater than y. If so, add 5 to y’s value,
# otherwise do nothing. Then, multiply z and y, and assign the resulting value to the variable x.
y = 22
z = 30
if z > y:
    y += 5
x = z * y
print(x)

# For each string in wrd_lst, find the number of characters in the string. If the number of characters is less than 6,
# add 1 to accum so that in the end, accum will contain an integer representing the total number of words in the list
# that have fewer than 6 characters.
wrd_lst = ["Hello", "activecode", "Java", "C#", "Python", "HTML and CSS", "Javascript", "Swift", "php"]
accum = 0
for wrd in wrd_lst:
    if len(wrd) < 6:
        accum += 1
print("the number of words that have fewer than 6 characters are",accum)
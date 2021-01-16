# The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total
# number of characters in the file and save to the variable num.
txt = open("travel_plans.txt")
txtR = txt.read()
num = len(txtR)
txt.close()

# We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total
# number of words in the file and assign this value to the variable num_words.
txt = open("emotion_words.txt")
txtR = txt.read().strip().split()
num_words = len(txtR)

# Assign to the variable num_lines the number of lines in the file school_prompt.txt.
txt = open("school_prompt.txt")
txtR = txt.readlines()
num_lines = len(txtR)

# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
txt = open("school_prompt.txt")
txtR = txt.read()
beginning_chars = txtR[:30]

# Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
txt = open("school_prompt.txt")
three = []
for line in txt:
    word = line.split()
    three.append(word[2])

# Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
txt = open("emotion_words.txt")
emotions = []
for line in txt:
    word = line.split()
    emotions.append(word[0])

# Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
txt = open("travel_plans.txt")
txtR = txt.read()
first_chars = txtR[:33]

# Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called
# p_words.
txt = open("school_prompt.txt")
p_words = []
for word in txt.read().split():
    if word.lower().count("p") > 0:
        p_words.append(word)
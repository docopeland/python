# Write a program that will print out the length of each item in the list as well as the first and last
# characters of the item.
weather = ["sunny", "cloudy", "partially sunny", "rainy", "storming", "windy", "foggy", "snowy", "hailing"]
for condition in weather:
    print("The word is", len(condition), "characters long")
    first_char = condition[0]
    last_char = condition[-1]
    print("The first character is", first_char)
    print("The last character is",last_char)

# Write code to determine how many t's are in the following sentences.
phrases = ["My, what a lovely day today is!", "Have you mastered cooking yet? A tasty treat could be in your future",
           "Have you ever seen the leaves change color?"]
for sentence in phrases:
    print(sentence.count("t"))
# Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports.
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports.insert(2,"horseback riding")
print(sports)

# Write code to take ‘London’ out of the list trav_dest.
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
trav_dest.remove("London")
print(trav_dest)

# Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method.
trav_dest.append("Guadalajara")
print(trav_dest)

# Write code to rearrange the strings in the list winners so that they are in alphabetical order from A to Z.
winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
winners.sort()
print(winners)

# Write code to switch the order of the winners list so that it is now Z to A. Assign this list to the variable
# z_winners.
winners.sort(reverse=True)
z_winners = winners[:]
print(z_winners)

# Currently there is a string called str1. Write code to create a list called chars which should contain the characters
# from str1. Each character in str1 should be its own element in the list chars.
str1 = "I love python"
chars = []
for cha in str1:
    chars.append(cha)
print(chars)

# For each character in the string saved in ael, append that character to a list that should be saved in a variable app.
ael = "python!"
app = []
for cha in ael:
    app.append(cha)
print(app)

#For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to
# a list called past_wrds.
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []
for wrd in wrds:
    past_wrds.append(wrd+"ed")
print(past_wrds)

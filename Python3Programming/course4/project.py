# This project will take you through the process of implementing a simplified version of the game Wheel of Fortune. Here
# are the rules of our game:
# There are num_human human players and num_computer computer players.
# Every player has some amount of money ($0 at the start of the game)
# Every player has a set of prizes (none at the start of the game)
# The goal is to guess a phrase within a category. For example:
# Category: Artist & Song | Phrase: Whitney Houston’s I Will Always Love You
# Players see the category and an obscured version of the phrase where every alphanumeric character in the phrase starts
# out as hidden (using underscores: _):
# Category: Artist & Song | Phrase: _______ _______'_ _ ____ ______ ____ ___
# Note that case (capitalization) does not matter
# During their turn, every player spins the wheel to determine a prize amount and:
# If the wheel lands on a cash square, players may do one of three actions:
# Guess any letter that hasn't been guessed by typing a letter (a-z)
# Vowels (a, e, i, o, u) cost $250 to guess and can’t be guessed if the player doesn’t have enough money. All other
# letters are “free” to guess
# The player can guess any letter that hasn’t been guessed and gets that cash amount for every time that letter appears
# in the phrase
# If there is a prize, the user also gets that prize (in addition to any prizes they already had)
# If the letter does appear in the phrase, the user keeps their turn. Otherwise, it’s the next player’s turn
# Example: The user lands on $500 and guesses ‘W’
# There are three W’s in the phrase, so the player wins $1500
# Guess the complete phrase by typing a phrase (anything over one character that isn’t ‘pass’)
# If they are correct, they win the game, if they are incorrect, it is the next player’s turn
# Pass their turn by entering 'pass'
# If the wheel lands on “lose a turn”, the player loses their turn and the game moves on to the next player
# If the wheel lands on “bankrupt”, the player loses their turn and loses their money but they keep all of the prizes
# they have won so far.
# The game continues until the entire phrase is revealed (or one player guesses the complete phrase)

# We’re going to define a few useful methods for you:
# getNumberBetween(prompt, min, max)) repeatedly asks the user for a number between min and max with the prompt prompt
# spinWheel() simulates spinning the wheel and returns a dictionary with a random prize
# getRandomCategoryAndPhrase() returns a tuple with a random category and phrase for players to guess
# obscurePhrase(phrase, guessed) returns a tuple with a random category and phrase for players to guess

import json
import random
import time
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Repeatedly asks the user for a number between min & max (inclusive)
def getNumberBetween(prompt, min, max):
    userinp = input(prompt) # ask the first time
    while True:
        try:
            n = int(userinp) # try casting to an integer
            if n < min:
                errmessage = 'Must be at least {}'.format(min)
            elif n > max:
                errmessage = 'Must be at most {}'.format(max)
            else:
                return n
        except ValueError: # The user didn't enter a number
            errmessage = '{} is not a number.'.format(userinp)
        # If we haven't gotten a number yet, add the error message
        # and ask again
        userinp = input('{}\n{}'.format(errmessage, prompt))

# Spins the wheel of fortune wheel to give a random prize
# Examples:
#    { "type": "cash", "text": "$950", "value": 950, "prize": "A trip to Ann Arbor!" },
#    { "type": "bankrupt", "text": "Bankrupt", "prize": false },
#    { "type": "loseturn", "text": "Lose a turn", "prize": false }
def spinWheel():
    with open("wheel.json", 'r') as f: # don't have the wheel.json file unfortunately
        wheel = json.loads(f.read())
        return random.choice(wheel)

# Returns a category & phrase (as a tuple) to guess
# Example: ("Artist & Song", "Whitney Houston's I Will Always Love You")
def getRandomCategoryAndPhrase():
    with open("phrases.json", 'r') as f: # don't have this file either
        phrases = json.loads(f.read())
        category = random.choice(list(phrases.keys()))
        phrase   = random.choice(phrases[category])
        return (category, phrase.upper())

# Given a phrase and a list of guessed letters, returns an obscured version
# Example:
#     guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
#     phrase:  "GLACIER NATIONAL PARK"
#     returns> "_L___ER N____N_L P_RK"
def obscurePhrase(phrase, guessed):
    rv = ''
    for s in phrase:
        if (s in LETTERS) and (s not in guessed):
            rv = rv+'_'
        else:
            rv = rv+s
    return rv

# Returns a string representing the current state of the game
def showBoard(category, obscuredPhrase, guessed):
    return """
Category: {}
Phrase:   {}
Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))

category, phrase = getRandomCategoryAndPhrase()

guessed = []
for x in range(random.randint(10, 20)):
    randomLetter = random.choice(LETTERS)
    if randomLetter not in guessed:
        guessed.append(randomLetter)

print("getRandomCategoryAndPhrase()\n -> ('{}', '{}')".format(category, phrase))
print("\n{}\n".format("-"*5))
print("obscurePhrase('{}', [{}])\n -> {}".format(phrase, ', '.join(["'{}'".format(c) for c in guessed]),
                                                 obscurePhrase(phrase, guessed)))
print("\n{}\n".format("-"*5))
obscured_phrase = obscurePhrase(phrase, guessed)
print("showBoard('{}', '{}', [{}])\n -> {}"
      .format(phrase, obscured_phrase, ','.join(["'{}'".format(c) for c in guessed]),
              showBoard(phrase, obscured_phrase, guessed)))
print("\n{}\n".format("-"*5))
num_times_to_spin = random.randint(2, 5)
print('Spinning the wheel {} times (normally this would just be done once per turn)'.format(num_times_to_spin))
for x in range(num_times_to_spin):
    print("\n{}\n".format("-"*2))
    print("spinWheel()")
    print(spinWheel())
print("\n{}\n".format("-"*5))
print("In 2 seconds, will run getNumberBetween('Testing getNumberBetween(). Enter a number between 1 and 10', 1, 10)")
time.sleep(2)
print(getNumberBetween('Testing getNumberBetween(). Enter a number between 1 and 10', 1, 10))

# MY CODES START HERE!!!
VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self, n,):
        self.name = n
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)

# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def __init__(self, n):
        WOFPlayer.__init__(self,n)

    def getMove(self, category, obscuredPhrase, guessed):
        move = input("""{} has ${}
        
        Category: {}
        Phrase:  {}
        Guessed: {}
        
        Guess a letter, phrase, or type 'exit' or 'pass':""".
                     format(self.name,self.prizeMoney,category,obscured_phrase,guessed))
        return move

# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = "ZQXJKVBPYGFWMUCLDRHSNIOATE"
    def __init__(self, n, diff):
        WOFPlayer.__init__(self,n)
        self.difficulty = diff

    def smartCoinFlip(self):
        rando = random.randint(1,10)
        if rando > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self, guessed):
        return [letter for letter in self.SORTED_FREQUENCIES if letter not in guessed
                if (letter in VOWELS and self.prizeMoney >= VOWEL_COST) or (letter not in VOWELS)]

    def getMove(self, category, obscuredPhrase, guessed):
        poss = self.getPossibleLetters(guessed)
        if poss == []:
            return "pass"
        else:
            if self.smartCoinFlip():
                return sorted(poss, key = lambda x: self.SORTED_FREQUENCIES.index(x),reverse = True)[0]
            else:
                return random.choice(poss)

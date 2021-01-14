# Use a for statement to print 10 random numbers.
import random
for _ in range(10):
    print(random.random())

# Repeat the above exercise but this time print 10 random numbers between 25 and 35.
for _ in range(10):
    print(random.randrange(25,35))
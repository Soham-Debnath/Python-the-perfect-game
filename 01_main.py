# The Perfect Guess

import random

n = random.randint(1,100)
a = -1
guesses = 0

while(a != n):
    guesses+=1
    a=int(input("enter your number: "))
    if(a>n):
        print("enter lower number")
    else:
        print("enter higher number")

print(f"you have guessed {n} in {guesses} attempts")
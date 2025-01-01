# The Perfect Guess

import random

n = random.randint(1,100)
a = -1
guesses = 1
 
while(a != n):
    
    a=int(input("enter your number: "))
    if(a>n):
        print("enter lower number")
        guesses+=1

    elif(a<n):
        print("enter higher number")
        guesses+=1

print(f"you have guessed {n} in {guesses} attempts")
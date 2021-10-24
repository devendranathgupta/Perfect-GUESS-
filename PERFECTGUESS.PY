#program for the perfect guess 
import random #random number for the random input from the user 
randomNumber  = random.randint(1,100)  #random number is between 1 and 100 
userguess = None 
guesses  = 0
while(userguess != randomNumber): #condition 1 
    userguess = int(input("Enter the Guess: "))
    guesses += 1
    if(userguess == randomNumber): #condition 2 
        print("Your guess is right ")
    else:
        if(userguess > randomNumber): #condition 3 
            print("You guessed it wrong ! Enter a Smaller number ")
        else:
            print("You guessed it wrong ! Enter a larger  number")    

print(f"You guessed the number in {guesses} in guesses")
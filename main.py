# I am creating the guessing game in python

#The program needs to have a range from 1 - 20 and also the computer needs to do this randomly. 


#Which functions does this? I am going to use trandom() function, which generates random numbers between 0 and 1 but in this case 1 - 20. 

import random

n = random.randint(1, 20)
# To play this game,the user have to guess and input a date. How do i prompt the user to input a data?
#The function input has an optional parameter, which is the prompt string.

# What do I want the prayer to do? Guess a from 1 - 20.
guess = int(input("Enter an integer from 1 to 20: "))

while n != "guess":

  print
#What do I want the computer to say If "the player" guess too low? or the guess is lower than the number that the computer is thinking. I want to say that the guess is low
  
  if guess < n:

    print ("guess is low")

    guess = int(input("Enter an integer from 1 to 20: "))
#What do I want the computer to say If "the player" guess too high? or the guess is higher than the number that the computer is thinking. I want to say that the guess is high
  elif guess > n:


    print ("guess is high")

    guess = int(input("Enter an integer from 1 to 20: "))

  else:
# What Do you I want the computer to say when I guess correctly? 

# Since I am the one playing, when i guess correctly, I want the computer to say...you guessed it Hampson!

    print ("you guessed it Hampson!")

# I am using the break statement because I once I gues correctly, I just want the computer to say so and nothing more. 

#Break statement in Python terminates the current loop. 


  break

  # If I dont use the break statement after i win it will keep saying ... you guessed it Hampson! over and over again. 

#you guessed it Hampson!
#you guessed it Hampson!
#you guessed it Hampson!
#you guessed it Hampson!
#you guessed it Hampson!
#you guessed it Hampson!
#you guessed it Hampson!

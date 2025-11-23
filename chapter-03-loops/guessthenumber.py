#This is a guess the number game
import random
secret_number=random.randint(1,20)  
print('i am thinking of a number between 1 and 20')

#ask the player to guess 6 times
for guesses_taken in range(1,7):
    print('Take a guess')
    guess=int(input('_'))

    #Check if the player input is less than or greater than the secret number
    if guess<secret_number:
        #print('Your guess is too low, you have ' + str(6- guesses_taken) + ' guesses left')
        print(f'Your guess is too low, you have {6-guesses_taken} guesses left')
    elif guess>secret_number:
        #print('Your guess is to high,you have' + str(6- guesses_taken) + ' guesses left')
        print(f'Your guess is too high, you have {6-guesses_taken} guesses left')
    else:
        break

if guess==secret_number:
    #print('Good job, you got it in '+ str(guesses_taken)+ 'th attempt')
    print(f"Good job, you got it in the {guesses_taken}'th attempt")
else:
    #print('Nope. the number is'+ str(secret_number))
    print(f"Nope. the number is {secret_number}")

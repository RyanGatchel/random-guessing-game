# Number guessing game in Python
## Ryan Gatchel ##

# Only have 6 guesses
# error handling for strings
# function

import random
random_number = random.randint(1,10)


print('RANDOM NUMBER GUESSING GAME')
def randomGuess():
    guess = 0
    try:
        while guess < 6:
            print('what is your guess?')
            answer = input()
            guess = guess + 1
            if guess >=6:
                print('YOU FAIL')
                break
            elif int(answer) == random_number:
                print('YOU WIN!')
                break
    except:
        print('please only numbers.')
        print('you can try again.')
        return randomGuess()

randomGuess()

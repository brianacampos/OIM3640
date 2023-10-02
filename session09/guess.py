# generate a random number between 1 and 50
import random


def number_guessing_game():
    number = random.randint(1, 51)

    # greet user and ask for their name
    player_name = input("Hello, What's your name?")

    # explain rules
    print('Well, ' + player_name + 'I am thinking of a number between 1 and 50:')

    # initial start of guesses is 0 when the game is reset
    number_of_guesses = 0

    # create while loop that increases guesses and tells user if input if too high or low
    while number_of_guesses < 6:
        # #this iteration will increase the number of guesses and output if their guess is too high or low
        # it will then break after the number of guesses has reached a limit of 6#
        guess = int(input())
        number_of_guesses += 1

        if guess < number:
            print('Your guess is too low.')
        elif guess > number:
            print('Your guess is too high.')
        else:
            break

    # if the guess is correct then it will let the player know
    if guess == number:
        print('Good job, ' + player_name + '! You guessed my number in ' +
              str(number_of_guesses) + 'tries!')
    else:
        print('Sorry, ' + player_name +
              ', you did not guess the number. The number was ' + str(number))


# Call the function to start the game
number_guessing_game()

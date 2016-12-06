import random

guesses_made = 0

name = input('Hello! What is your name?\n')

number = random.randint(1, 20)
print('Well, {0}, I am thinking of a number between 1 and 20.'.format(name))

qtde_guesses_made = int(input('How many chances do you want? (Between 3 and 5) '))

if qtde_guesses_made > 5:
    print("Don't try to cheat at me, looser!")
else:
    if qtde_guesses_made < 3:
        print("you are a hero or a dummy guy")
    while guesses_made < qtde_guesses_made:

        guess = int(input('Take a guess: '))

        guesses_made += 1
        if guess < number:
            print ('Your guess is too low.')


        if guess > number:
            print ('Your guess is too high.')

        if guess == number:
            break

    if guess == number:
      print ('Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made))
    else:
        print ('Nope. The number I was thinking of was {0}'.format(number))

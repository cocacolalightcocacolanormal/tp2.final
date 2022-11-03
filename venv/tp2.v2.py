# tp2

import random


def number():
    nombre1 = int(input('Vous devez choisir entre deux nombre, choisissez le premier'))
    nombre2 = int(input('Vous devez choisir entre deux nombres, choisissez le second'))
    return random.randint(nombre1, nombre2)


playing = True
while playing:
    range = number()
    winning = False
    tries = 0
    while not winning:
        tries += 1

        guess = int(input('Essayez de deviner le nombre entre les nombres que vous avez choisis'))

        if guess > range:
            print('Votre nombre est trop grand, choisissez un plus petit')
        elif guess < range:
            print('Votre nombre est trop petit, choisissez un plus grand')
        else:
            print('Vous avez fini en:', tries)
            winning = True
    question = input('Est-ce que vous voulez recommencer y/n')
    if question == 'n':
        print("Bye")
        playing = False
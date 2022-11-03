# tp2

import random

#On crée une fonction qui crée les bornes de la devinette
def nombre():
    nombre1 = int(input('Bienvenue à un jeu de devinette. Vous devez choisir deux nombres, et ensuite deviner un nombre aléatoire qui est entre ces deux nombres.'
                        'Choisissez le premier'))
    nombre2 = int(input('Choisissez le deuxième'))
    #On choisit le nombre aléatoire entre les paramètres des bornes
    return random.randint(nombre1, nombre2)


playing = True
while playing:
    range = nombre()
    winning = False
    tries = 0
    while not winning:
        tries += 1
#On crée la variable de "guess", qui est le nombre deviné par l'utilisateur
        guess = int(input('Essayez de deviner le nombre entre les nombres que vous avez choisis'))
#Si le nombre est trop grand comparé au nombre mystère, on demande au programme de le dire à l'utilisateur
        if guess > range:
            print('Le nombre que vous avez deviné est trop grand, choisissez un plus petit')
        # Si le nombre est trop petit comparé au nombre mystère, on demande au programme de le dire à l'utilisateur
        elif guess < range:
            print('Le nombre que vous avez deviné est trop petit, choisissez un plus grand')
            #Si le nombre deviné s'agit du nombre mystère, on le dit à l'utilisiateur ainsi que le nombre d'essais utilisés
        else:
            print('Vous avez fini en:', tries, 'essais')
            winning = True
    question = input('Voulez-vous recommencer? Si oui, appuyez sur Y. Si non, appuyez sur N.')
    if question == 'n':
        print("Merci, bye")
        playing = False
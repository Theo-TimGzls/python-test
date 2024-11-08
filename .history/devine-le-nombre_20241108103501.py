import random import randint

def jeu():
    nombre_aléatoire = randint(1,100)
    nombre= 0
    coups = 0

while nombre != nombre_aléatoire:
    nombre= int(input('entrer votre nombre'))

    if nombre==nombre_aléatoire:
        print('Bien joué')
    elif nombre > nombre_aléatoire:
        print('Trop grand')
        life-=1
    else nombre < nombre_aléatoire:
        print('Trop petit')
        life-=1

    if life==0:
        print('Perdu..')
    
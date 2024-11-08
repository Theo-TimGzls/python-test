from random import randint

def jeu():
    nombre_aléatoire = randint(1,100)
    nombre= 0
    coups = 0

while nombre != nombre_aléatoire:
    nombre= int(input('entrer votre nombre'))
    coups += 1
    if nombre < nombre_aléatoire
        print("C'est moins.")
    elif nombre > nombre_aléatoire:
        print("C'est plus.")
    else: print("Gagné en {coups} coups.")
    
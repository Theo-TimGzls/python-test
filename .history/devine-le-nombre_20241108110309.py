import random

nombre_aleatoire = random.randint(1,100)
nombre= 0
coups = 0


while nombre != nombre_aleatoire:
    nombre= int(input('entrer votre nombre : '))
    coups += 1
    if nombre < nombre_aleatoire:
        print("C'est plus.")
    elif nombre > nombre_aleatoire:
        print("C'est moins.")
    else: print("Gagné en {coups} coups.")
    
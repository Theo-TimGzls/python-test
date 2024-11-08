import random

nombre_aléatoire = random.randint(1,100)

nombre=""

life = 10

while nombre != nombre_aléatoire:
    nombre= int(input('entrer votre nombre'))

    if nombre==nombre_aléatoire:
    print("Bien joué")
    break
    if nombre > nombre_aléatoire:
    print('Trop grand')
    life -=1
    if nombre < nombre_aléatoire:
    print('Trop petit')
    life -=1

    if life==0:
        print('Perdu..')
        break
    
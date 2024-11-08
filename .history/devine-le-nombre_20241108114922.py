import random

nombre_aleatoire = random.randint(1,100)
nombre = 0
coups = 0
nbr_essais_max = 5
nbr_essais = 1

while nombre != nombre_aleatoire:
    nombre= int(input('entrer votre nombre : '))
    coups += 1
    if nombre < nombre_aleatoire:
        print("C'est plus.")
    elif nombre > nombre_aleatoire:
        print("C'est moins.")
    else: print("Gagné")
    nbr_essais += 1
    
if nbr_essais>nbr_essais_max and ton_nombre != mon_nombre :
    print("Désolé, vous avez utilisé vos",nbr_essais_max,"essais en vain.")
    print("J'avais choisi le nombre",mon_nombre,".")

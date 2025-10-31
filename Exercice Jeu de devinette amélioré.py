from random import randrange

x = (randrange(0, 101))
a=0
m=int(input(("Tente de trouver le nombre que j'ai en tête :")))
nombre_choisis=[]

while a == 0:

    if m in nombre_choisis:
        print("Tu ne sembles pas être le pingouin glissant le plus loin...")
        print("Tu avais déjà essayé cette réponse...")
        print(message)
        print()
        m = int(input("Tente de trouver le nombre que j'ai en tête :"))
        continue


    if m == x:
        a=1
        print("Bravo humain, vous avez trouvé le nombre !!!")

    if m > x:
        message = "Plus bas !!"
        print(message)
        nombre_choisis.append(m)
        print()
        m = int(input("Tente de trouver le nombre que j'ai en tête :"))


    if m < x:
        message = "Plus haut !!"
        print(message)
        nombre_choisis.append(m)
        print()
        m = int(input("Tente de trouver le nombre que j'ai en tête :"))
import math
def addition():
    num1=float(input("Donnez un nombre : "))
    num2=float(input("Donnez un nombre : "))
    résultat = num1+num2
    print(f"Le résultat de {num1} + {num2} équivaut à {résultat}")
def multiplication():
    num1=float(input("Donnez un nombre : "))
    num2=float(input("Donnez un nombre : "))
    résultat = num1*num2
    print(f"Le résultat de {num1} x {num2} équivaut à {résultat}")
def soustraction():
    num1=float(input("Donnez un nombre : "))
    num2=float(input("Donnez un nombre : "))
    résultat = num1-num2
    print(f"Le résultat de {num1} - {num2} équivaut à {résultat}")
def division():
    num1=float(input("Donnez un nombre : "))
    num2=float(input("Donnez un nombre : "))
    if num2==0:
        print("Erreur: Un nombre ne peut être divisé par 0 .")
    else:
        résultat = num1/num2
        print(f"Le résultat de {num1} / {num2} équivaut à {résultat}")
def puissance():
    num1=float(input("Donnez un nombre : "))
    num2=float(input("Donnez un nombre : "))
    résultat = num1**num2
    print(f"Le résultat de {num1}**{num2} équivaut à {résultat}")
def racine():
    num1=float(input("Vous voulez connaître la racine carré de quel nombre ? "))
    if num1 < 0:
        print("Erreur : La racine carrée d'un nombre négatif n'est pas définie.")
    else:
        résultat= math.sqrt(num1)
        print(f"La racine carrée de {num1} est : {résultat} .")
choix = input("Voulez vous calculer la racine carré d'un nombre ?(oui/non) ").lower()
if choix == "oui":
    racine()
elif choix== "non":
    operateur = input("Entrer un opérateur ( + ; - ; * ; / ; ** ) : ")
    if operateur == "+":
        addition()
    elif operateur == "-":
        soustraction()
    elif operateur == "*":
        multiplication()
    elif operateur == "/":
        division()
    elif operateur == "**":
        puissance()
    else:
        print("L'opérateur n'est pas valide")
else:
    print("Votre choix n'est pas valide .")
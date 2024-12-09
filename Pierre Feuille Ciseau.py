import random

print("Partie de pierre ,feuille ,ciseau.\n----------------------------------")

options = ("Pierre", "Feuille", "Ciseau")

scoreJoueur=0
scoreOrdinateur=0
totalParties=0
matchNul=0
joueur=""
while True:
    joueur=""
    while joueur not in options :
        joueur = input("Veuillez entrer votre choix : ").capitalize()
    ordinateur = random.choice(options)
    print(f"Ordinateur : {ordinateur}")
    print(f"joueur : {joueur}")
    if joueur == ordinateur:
        print("Match nul!")
        matchNul+=1
        totalParties+=1
    elif joueur == "Ciseau" and ordinateur == "Pierre" or joueur == "Feuille" and ordinateur == "Ciseau" or joueur == "Pierre" and ordinateur == "Feuille"  :
        print("L'ordinateur gagne la partie !")
        scoreOrdinateur+=1
        totalParties+=1
    elif ordinateur == "Ciseau" and joueur == "Pierre" or  ordinateur == "Feuille" and joueur == "Ciseau" or ordinateur == "Pierre" and joueur == "Feuille" :
        print("Le joueur gagne la partie !")
        totalParties+=1
        scoreJoueur+=1
    else:
        print("Erreur")

    rejouer=input("Voulez-vous rejouer ? (oui/non) : ").lower()
    if rejouer == "oui":
        print("Merci de rejouer.")
    if rejouer == "non":
        break

print(f"Vous avez joué un total de {totalParties} parties.\n"
      f"Vous avez fait {matchNul} match nul.\n"
      f"Vous avez eu un score de {scoreJoueur}.\n"
      f"L'ordinateur a eu un score de {scoreOrdinateur}\n"
      "Merci d'avoir joué .")
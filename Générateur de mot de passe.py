import random
import string
print("Générateur de mot de passe .\n"
      "----------------------------")

caractères_spéciaux_basiques = ".;,!?%-_"
ensemble = ""
lettre=input("Voulez vous des lettres dans votre mot de passe (oui/non) ? ").lower()
chiffre=input("Voulez vous des chiffres dans votre mot de passe (oui/non) ? ").lower()
spécial=input("Voulez vous des caractères spéciaux dans votre mot de passe (oui/non) ? ").lower()
if lettre == "oui":
    ensemble += string.ascii_letters
if chiffre == "oui":
    ensemble += string.digits
if spécial == "oui":
    ensemble += caractères_spéciaux_basiques
x = int(input("Quelle est la longueur de votre mot de passe ?\n"))
mdp=[]
for caractère in range(x):
    aléatoire = random.choice(ensemble)
    mdp.append(aléatoire)
print(f"Votre mot de passe est : {''.join(mdp)} ")
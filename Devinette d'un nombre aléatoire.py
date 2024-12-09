import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    essai = 0
    while guess != random_number:
        guess = int(input("Choisissez un nombre entre 1 et 10 : "))
        if guess > x or guess < 1:
            print("Veuillez rentrer un nombre valide .")
        elif guess > random_number:
            print("Trop haut , réessayez .")
            essai+=1
        elif guess < random_number:
            print("Trop bas , réessayez .")
            essai+=1
        if guess == random_number:
            essai+=1
            print(f"Vous avez réussi en {essai} essais ,bravo!")
guess(10)
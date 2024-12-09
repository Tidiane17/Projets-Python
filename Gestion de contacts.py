print("Gestion de contacts :\n"
      "---------------------")

contacts = []
class Contacts:
    def __init__(self, nom, num):
        self.nom = nom
        self.num = num
    def __str__(self):
        return f"{self.nom} : {self.num}"
    
while True:
    option = str(input("Que voulez vous faire ? (1/2/3/4)\n"
                   "1.Afficher vos contacts\n"
                   "2.Ajouter un contact\n"
                   "3.Supprimer un contact\n"
                   "4.Quitter\n"))
    
    if option == "1":
        for contact in contacts:
            print(contact)

    elif option == "2":
        prenom = str(input("Quelle est le nom de votre contact ? "))
        numero = str(input("Quelle est le numero de votre contact ? "))
        contacts.append(Contacts(prenom, numero))
        print()

    elif option == "3":
        nom_a_supprimer = input("Entrez le nom du contact à supprimer : ")
        contact_trouve = None
        for contact in contacts:
            if contact.nom == nom_a_supprimer:
                contact_trouve = contact
                break
        if contact_trouve:
            contacts.remove(contact_trouve)
            print(f"Le contact {nom_a_supprimer} a été supprimé.")
        else:
            print(f"Le contact {nom_a_supprimer} n'existe pas.")
            
    elif option == "4":
        break
    else:
        print("Rentrez une option valide .")
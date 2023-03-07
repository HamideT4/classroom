from ClassroomApp.models import Etudiant, Groupe, Commande
import csv

def run():
    with open('ClassroomApp/classroom.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Etudiant.objects.all().delete()
        Groupe.objects.all().delete()

        for row in reader:
            print(row)

            groupe, _ = Groupe.objects.get_or_create(nom = row [7])

            etudiant, _ = Etudiant.objects.get_or_create(
                nom = row[1],
                prenom = row[2],
                genre = row[3],
                email = row[4],
                telephone = row[5],
                photo = row[6],
                groupe = groupe
            )

            commande, _ = Commande.objects.get_or_create (
                menu = row [8],
                quantite = row [9],
                groupe = groupe,
                etudiant = etudiant
            )
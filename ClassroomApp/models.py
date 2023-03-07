from django.db import models

class Groupe(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class Etudiant(models.Model):
    Genre = (
        ('Male', ('Male')),
        ('Female', ('Female')),
    )
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=200)
    genre = models.CharField(max_length=32, choices=Genre)
    email = models.CharField(max_length=250)
    telephone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='static/photo', blank=True)
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.nom

class Commande(models.Model):
    Menu = (
        ('Haricot', ('Haricot')),
        ('Riz', ('Riz')),
        ('Pâtes', ('Pâtes')),
        ('Soupe', ('Soupe')),
        ('Aucun', ('Aucun')),
    )
    menu = models.CharField(max_length=200, choices=Menu, default="", blank=True)
    quantite = models.IntegerField(default=0)
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE, blank=True)
    etudiant = models.OneToOneField(Etudiant, on_delete=models.CASCADE)

    def __str__(self):
        return self.menu
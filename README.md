# classroom

## Commandes utiles :

* Faire la mise à jour :
  * se positionner sur la branche main avec : $ git checkout main
  * recupérer les mises à jour de la branche main: $ git pull https://github.com/HamideT4/classroom main
  * recupérer les mises à jour de la branche nom_branche: $ git pull https://github.com/HamideT4/classroom nom_branche
  * appliquer les mises à jour à sa brache : 
    1. git checkout nom_branche_personnel
    2. git merge main
  * envoyer son travail sur sa branche distante : $ git push
  
* Après avoir fait des mises à jour, faire un pull request via l'interface de GitHub.

## .env :
  * Créer un fichier .env
  * Y ajouter les lignes suvantes :
    - DB_NAME = 'nom_de_la_base_des_données'
    - DB_USER = 'root'
    - DB_PASS = 'votre_mot_de_passe_mysql'.
  
  Ainsi les nouvelles configurations de la variable DATABASE de settings.py ne générera pas d'erreur.

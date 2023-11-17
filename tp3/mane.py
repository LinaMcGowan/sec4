import random

niveau_vie=20
numero_adversaire=0
numero_combat=0
nombre_defaites=0
nombre_victoires_consecutifs=0
nombre_victoires=0
choix='none'
while choix!=4:


   force_adversaire  = random.randint (1,5)
   print("force_adversaire")
   print("1- Combattre cet adversaire 2- Contourner cet adversaire et aller ouvrir une autre porte 3- Afficher les règles du jeu 4- Quitter la partie")
   choix=input("quel est ton choix")
   if choix== "1":
      numero_adversaire+=1
      numero_combat+=1
      de=random.randint(1,6)
      print(de)
      if force_adversaire>=de:
          #perdu
         niveau_vie=niveau_vie+force_adversaire
         nombre_defaites+=1
         print("perdu")
         nombre_victoires_consecutives=0
      if force_adversaire <=de:
          #gagné
         niveau_vie=niveau_vie+force_adversaire
         nombre_victoires+=1
         nombre_victoires_consecutives+=1
         print("gagné")
         print("niveau_vie=20")
   numero_adversaire+=1
   numero_combat+=1
   nombre_defaites=0
   nombre_victoires_consecutifs+=1
   if niveau_vie<=0:
       print("dead")
       quit()
   if niveau_vie>0:
       print("vie+nombre_victoires_consecutives")

   if choix=="2":
      niveau_vie-=1
      print("vie")
   if choix=="3":
         print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.La partie se termine lorsque les points de vie de l’usager tombent sous 0. L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")
   if choix=="4":
      print("merci")
      quit()


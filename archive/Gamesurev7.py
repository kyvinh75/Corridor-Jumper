import pygame
import sys
import random
import time # temps pour le chrono 
import tkinter  # interface graphique, police , taille du texte
from pygame.locals import *

pygame.init()




#Variables du jeu
maintain=True #Maintiens le jeu ouvert
scrolling=0 #A quel point le jeu défile, définit le score
speed=1

print("\nCeci est une version de développement et ne dois en aucun cas être considérée comme le produit final.\n")
print ("Crédits : KY-VINH NGUYEN / LSUPERMAN735, ETIENNE BARBOSA, ARTHUR SOUILLE ")#Affiche les crédits BY KV
print ("Crédits : KV , EB, AS")
#Affichage de la fenêtre
#déclaration de la longueur et de la largeur afin de modifier plus rapidement by KV
length =400 #longueur attribuée à 400 pour être petite
width = 550#largeur attribuée à 550
window=pygame.display.set_mode((length,width))
info=pygame.display.Info()
pygame.display.set_caption("Corridor Jumper") #définit le titre de la fenêtre
pygame.mouse.set_visible(False) # permet de masquer la souris by KV

#en théorie il devait afficher un fond en rouge mais l'image prend le dessus by KV
#red = [255, 0, 0]
#window.fill(red)

#Chargements
#   Variables dans lesquelles on stock les images
background=[]
player=[]
obstacle=[]
#chronomètre malheureusement échoué by KV



#Charger une musique de fond by KV
_music=['music1.mp3','music2.mp3','music3.mp3','music4.mp3'] #musique stockée manuellement attention la liaisoon n'est pas fini ! car il y a une erreur
pygame.mixer.init() #permet d'initialiser le lecteur musicale
pygame.mixer.music.load('data\music.mp3')# permet de charger la musique SOMETHING ABOUT YOU de HAYDEN JAMES 
pygame.mixer.music.set_volume(0.89) #le volume est à 89%
pygame.mixer.music.play(-1,0) # répétition, start -1 permet de répéter la musique à l'infini et play permet de jouer la musique

#   Boucles ou on stock les images dans les variables précédentes
#       Backgrounds
for i in range(0,1):
    try:
        print("Chargement de data/Back_"+str(i)+".png")
        background.append(pygame.image.load("data/Back_"+str(i)+".png"))

        
    except:
        print("Une erreur est survenue\nFermeture du programme...")
        sys.exit()
#       Player
for i in range(0,1):
    try:
        print("Chargement de data/Player_"+str(i)+".png")
        player.append(pygame.image.load("data/Player_"+str(i)+".png"))
    except:
        print("Une erreur est survenue\nFermeture du programme...")
        sys.exit()
#       Obstacles
for i in range(0,3):
    try:       
        print("Chargement de data/Obstacle_"+str(i)+".png")
        obstacle.append(pygame.image.load("data/Obstacle_"+str(i)+".png"))
    except:
        print("Une erreur est survenue\nFermeture du programme...")
        sys.exit()

print("\nEn cours...\n")
print("Détails:")
print("Facteur vitesse: "+str(speed))

type_obstacle=[]
pos_obstacle=[]
offset_obstacle=[]
generated=False #La postition initiale des obstacle a elle ete generee?
player_pos_x=180 #Position du joueur sur l'axe x

#Boucle du jeu
while maintain:

    scrolling=scrolling+speed #Fait défiler le fond
    window.blit(background[0],(0,scrolling-9450)) #Fait afficher le fond

    if generated==False: #Genere la position initiale des obstacles
        for i in range(0,5):
            type_obstacle.append(random.randrange(0,3,1)) #Le type des obstacles (chaise? extincteur?)
            pos_obstacle.append(random.randrange(130,231,50)) #La position des obstacles (dans quelles colonnes sont ils?)
            offset_obstacle.append(random.randrange(scrolling-40,scrolling-1000,-40)) #Difficultés avec randrange, ne prend en charge que des ints
        generated=True
    for i in range(0,5): #Regarde si des obstacles sont hors du champs de vision
        if scrolling+offset_obstacle[i]>550:
            offset_obstacle[i]=offset_obstacle[i]+random.randrange(-600,-2000,-40)  #Affiche les obstacles supplémentaires
            pos_obstacle[i]=random.randrange(130,231,50)
    for i in range(0,5): #Affiche les obstacles
        window.blit(obstacle[type_obstacle[i]],(pos_obstacle[i],scrolling+offset_obstacle[i]))

    window.blit(player[0],(player_pos_x,500)) #Affiche le joueur
    for i in range(0,5): #Vérifie si le joueur marche sur un obstacle et arrête l'app si c'est le cas
        if player_pos_x==pos_obstacle[i] and scrolling+offset_obstacle[i]==460:
            maintain=False
    
    if scrolling/100>100: #Vérifie qu'on est pas à la fin du niveau
        print("Gagné !")
        maintain=False
    
    pygame.display.flip() #Met à jour la vue

#le code bugguait seule la touche espace ou l'inverse marche les autres sont bizarres la boucle était visiblement mal isolée
# corrigé il fallait placé la flèche espace après l'usage de la flèche droite et la flèche
    for event in pygame.event.get():
        if event.type==KEYDOWN and event.key==K_RIGHT: #Traite la flèche DROITE
            if player_pos_x==230: #Restriction des mouvements
                print("Deplacement à droite impossible.")
            else:
                player_pos_x=player_pos_x+50
        if event.type==KEYDOWN and event.key==K_LEFT: #Traite la flèche GAUCHE
            if player_pos_x==130: #Restriction des mouvements
                print("Deplacement à gauche impossible.")
            else:
                player_pos_x=player_pos_x-50
        if event.type==KEYDOWN and event.key==K_SPACE : #Traite la flèche ESPACE
            speed = speed +1
            print (str(speed))
            if speed == 10:#Donc la vitesse max est à 9 il vaudrait mieux mettre 11 car la vitesse sera figée lorsqu'il atteint la vitesse 10 mais c'est choix plus qu'un bug
                speed=0
            if event.type==QUIT: #Traite la fin du programme
                maintain=False
   
    pygame.display.set_caption("Corridor Jumper - "+str(int(scrolling/100))+"%")


print("\nNiveau completé à "+str(int(scrolling/100)) +"%")
#AUTRES VARIABLES by KV
player_name=[] # permettra d'attriuer un nom au joueur
player_satisfaction=[] # permettra d'obtenir la satisfaction du joueur 
player_name=input("nom du joueur : ")#permet l'attribution du nom du joueur by KV
player_satisfaction =input("Alors à quel point ce jeu vous a plus un peu, beaucoup ou énormément : ")
print("\nArrêt...")
sys.exit() 


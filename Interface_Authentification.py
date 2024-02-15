import pygame
import pygame.locals
from Bouton import Button
from Login_Inscription import Authentification

pygame.init()
pygame.mixer.init()

#Fenetre
screen_height = 700
screen_width = 1200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sficord')

#Variables Couleurs et Texte
blue ="#143263"
white="#ffffff"

connexion_button = Button("Connexion", (50, 170), (30, 35),Authentification.login(), color=white)

#Variables images
background = pygame.image.load('Data/Pictures/ghibli_background.jpg')
background = pygame.transform.scale(background,(screen_width+600,screen_height))


#Variables son
pygame.mixer.music.load('Data/Song/Ghibli_song.mp3')
pygame.mixer.music.play(-1)

def Interface():
    font_title = pygame.font.Font("Data/Font/MickeyMouse.otf", 200)
    titre_texte = font_title.render('Sficord', True, white)
    titre_rect = titre_texte.get_rect(center=(screen_width // 2, 200))

    

    screen.blit(background,(0,0))
    screen.blit(titre_texte, titre_rect)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    connexion_button.handle_event(event)
    connexion_button.draw(screen)

        
    Interface()
    pygame.display.update()

pygame.quit()
    

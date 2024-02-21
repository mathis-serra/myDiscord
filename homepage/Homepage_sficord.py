import pygame
import pygame_gui

pygame.init()
pygame.mixer.init()

# Fenetre
screen_height = 700
screen_width = 1200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sficord')

# Variables Couleurs et Texte
blue = "#143263"
white = "#ffffff"
font_before = pygame.font.Font("Data/Font/MickeyMouse.otf", 45)
email_text_render = font_before.render("Email :", True, white)
email_text_rect = email_text_render.get_rect(topleft=(260, 300))
password_text_render = font_before.render("Password :", True, white)
password_text_rect = password_text_render.get_rect(topleft=(200, 362))
nom_text_render = font_before.render("Nom :", True, white)
nom_text_rect = nom_text_render.get_rect(topleft=(280, 420))
prenom_text_render = font_before.render("Prenom :", True, white)
prenom_text_rect = password_text_render.get_rect(topleft=(235, 482))



# Boutons et images

background = pygame.image.load('Data/Pictures/ghibli_background.jpg')
background = pygame.transform.scale(background, (screen_width+600, screen_height))  

pygame.mixer.music.load('Data/Song/Ghibli_song.mp3')
pygame.mixer.music.play(-1)



run = True
interface_first=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()

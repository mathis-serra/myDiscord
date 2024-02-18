import pygame
import pygame_gui
from Bouton import Button
from Login_Inscription import Authentification

pygame.init()
pygame.mixer.init()

# Fenetre
screen_height = 700
screen_width = 1200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sficord')

# Interface de pygame_gui
manager = pygame_gui.UIManager((screen_width, screen_height))
email_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400, 300), (400, 40)),
                                                  manager=manager)
# Nouvelle zone de saisie juste en dessous de la zone de saisie de l'email
password_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400, 360), (400, 40)),
                                                     manager=manager)

# Variables Couleurs et Texte
blue = "#143263"
white = "#ffffff"
font_before = pygame.font.Font("Data/Font/MickeyMouse.otf", 45)
email_text_render = font_before.render("Email :", True, white)
email_text_rect = email_text_render.get_rect(topleft=(260, 300))
password_text_render = font_before.render("Password :", True, white)
password_text_rect = password_text_render.get_rect(topleft=(200, 362))


# Fonction de connexion
def handle_login():
    email = email_entry.get_text()
    password = password_entry.get_text()
    result = Authentification().login(email, password)
    if result["success"]:
        print("Connexion réussie !")
    else:
        print("Échec de la connexion :", result["message"])

# Boutons et images
connexion_button = Button("Connexion", (300, 600), (36, 15), handle_login, white, width=200, height=55)
inscription_button = Button("Inscription", (700, 600), (36, 15), Authentification(), white, width=200, height=55)
register_image = pygame.image.load('Data/Pictures/register.png')
register_image = pygame.transform.scale(register_image, (320, 100))
login_image = pygame.image.load('Data/Pictures/login.png')
login_image = pygame.transform.scale(login_image, (265, 210))
background = pygame.image.load('Data/Pictures/ghibli_background.jpg')
background = pygame.transform.scale(background, (screen_width+600, screen_height))  

# Variables son
pygame.mixer.music.load('Data/Song/Ghibli_song.mp3')
pygame.mixer.music.play(-1)

def Interface1():
    font_title = pygame.font.Font("Data/Font/MickeyMouse.otf", 200)
    titre_texte = font_title.render('Sficord', True, white)
    titre_rect = titre_texte.get_rect(center=(screen_width // 2, 200))
    screen.blit(background, (0, 0))
    screen.blit(email_text_render, email_text_rect)
    screen.blit(password_text_render, password_text_rect)
    connexion_button.draw(screen)
    inscription_button.draw(screen)
    screen.blit(register_image, (640, 575))
    screen.blit(login_image, (265, 500))
    manager.update(0.01)
    manager.draw_ui(screen)
    screen.blit(titre_texte, titre_rect)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        manager.process_events(event) 
        connexion_button.handle_event(event)
        inscription_button.handle_event(event)

    Interface1()
    pygame.display.update()

pygame.quit()

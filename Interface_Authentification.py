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
nom_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400, 420), (400, 40)),
                                                    manager=manager)
prenom_entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400, 480), (400, 40)),
                                                    manager=manager)
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


# Fonction de connexion et Interface
def handle_login():
    email = email_entry.get_text()
    password = password_entry.get_text()
    print(email,password)
    result = Authentification().login(email, password)
    if result["success"]:
        print("Connexion réussie !")
    else:
        print("Échec de la connexion :", result["message"])

def handle_register():
    email = email_entry.get_text()
    password = password_entry.get_text()
    nom = nom_entry.get_text()
    prenom = prenom_entry.get_text()
    print(email,password,nom,prenom)

    result = Authentification().register(email, password, nom, prenom)

    if result["success"]:
        print("Inscription réussie !")
    else:
        print("Échec de l'inscription :", result["message"])

def hide_entry():
    nom_entry.hide()
    prenom_entry.hide()

def show_entry():
    nom_entry.show()
    prenom_entry.show()

def Interface2():
    global interface_first

    screen.fill((0, 0, 0))
    
    interface_first=False
    font_title = pygame.font.Font("Data/Font/MickeyMouse.otf", 200)
    titre_texte = font_title.render('Sficord', True, white)
    titre_rect = titre_texte.get_rect(center=(screen_width // 2, 200))
    inscription2_button.draw(screen)
    screen.blit(background, (0, 0))
    screen.blit(email_text_render, email_text_rect)
    screen.blit(password_text_render, password_text_rect)
    screen.blit(nom_text_render, nom_text_rect)
    screen.blit(prenom_text_render, prenom_text_rect)
    screen.blit(register_image, (250, 435))
    manager.draw_ui(screen)
    screen.blit(titre_texte, titre_rect)
    manager.update(0.01)
    pygame.display.flip()

# Boutons et images
connexion_button = Button("Connexion", (300, 560), (36, 15), handle_login, white, width=200, height=100)
inscription_button = Button("Inscription", (700, 550), (36, 15), Interface2, white, width=200, height=100)
inscription2_button = Button("Inscription2", (500, 550), (36, 15), handle_register, white, width=200, height=100)
register_image = pygame.image.load('Data/Pictures/register.png')
register_image = pygame.transform.scale(register_image, (730, 350))
login_image = pygame.image.load('Data/Pictures/login.png')
login_image = pygame.transform.scale(login_image, (265, 210))
background = pygame.image.load('Data/Pictures/ghibli_background.jpg')
background = pygame.transform.scale(background, (screen_width+600, screen_height))  

# Variables son
pygame.mixer.music.load('Data/Song/Ghibli_song.mp3')
pygame.mixer.music.play(-1)

def Interface1():
    global interface_first

    interface_first=True
    font_title = pygame.font.Font("Data/Font/MickeyMouse.otf", 200)
    titre_texte = font_title.render('Sficord', True, white)
    titre_rect = titre_texte.get_rect(center=(screen_width // 2, 200))
    connexion_button.draw(screen)
    inscription_button.draw(screen)
    screen.blit(background, (0, 0))
    screen.blit(email_text_render, email_text_rect)
    screen.blit(password_text_render, password_text_rect)
    screen.blit(register_image, (440, 435))
    screen.blit(login_image, (265, 500))
    manager.update(0.01)
    manager.draw_ui(screen)
    screen.blit(titre_texte, titre_rect)
    hide_entry()


run = True
interface_first=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        manager.process_events(event) 
        inscription_button.handle_event(event)


    if interface_first:
        connexion_button.handle_event(event)
        Interface1()
    else:
        inscription2_button.handle_event(event)
        show_entry()
        Interface2()

    
    manager.update(0.01)

    pygame.display.update()

pygame.quit()

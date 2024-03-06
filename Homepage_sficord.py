import pygame

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
grey="#5c5959"
green="#396b3b"
font_before = pygame.font.Font("Assets/Font/MickeyMouse.otf", 45)

# Boutons et images
background = pygame.image.load('Assets/Pictures/home_background.png')
background = pygame.transform.scale(background, (screen_width, screen_height))  

pygame.mixer.music.load('Assets/Song/Ghibli_song.mp3')
pygame.mixer.music.play(-1)

#rectangle
rect_height = screen_height - 90
rect_width = 300
rect_x = 50
rect_y = 50
corner_radius = 30

#cercle
circle_radius = 40
circle_center = (110, 120)

run = True
interface_first=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, grey, (rect_x, rect_y, rect_width, rect_height), border_radius=corner_radius)
    pygame.draw.circle(screen, white, circle_center, circle_radius)

    pygame.display.update()

pygame.quit()

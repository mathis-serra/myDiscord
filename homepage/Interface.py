import pygame
from BasepageInterface import BasePage

def main():
    pygame.init()
    pygame.mixer.init()

    # Fenetre
    screen_height = 700
    screen_width = 1200
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Sficord')

    base_page = BasePage(screen)

    while base_page.run:
        base_page.handle_events()
        base_page.update()

    pygame.quit()

if __name__ == "__main__":
    main()

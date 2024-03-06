import pygame
from homepage.BasepageInterface import BasePage

#Child of the BasePage class, which lets you create a rectangle and change your profile photo on the application.
class Profil(BasePage):
    def __init__(self,screen):
        super().__init__(screen)

    #Create a rectangle to change photos
    def new_rect(self):
        pygame.draw.rect(self.screen, self.beige, (500, 100,500,self.screen_height - 200), border_radius=30)
        pygame.display.update()


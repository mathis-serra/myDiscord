import pygame
from BasepageInterface import BasePage

class Messages(BasePage):
    def __init__(self,screen):
        super().__init__(screen)

    def new_rect(self):
        pygame.draw.rect(self.screen, self.beige, (500, 50,500,self.screen_height - 90), border_radius=30)
        pygame.display.update()

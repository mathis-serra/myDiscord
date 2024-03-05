import pygame

from homepage.Bouton import Button
from Login_Inscription import Authentification



class BasePage():
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.grey="#5c5959"
        self.white="#ffffff"
        self.blue = "#1769aa"
        self.beige="#d0c8b6"
        self.font_before = pygame.font.Font("Assets/Font/MickeyMouse.otf", 45)
        self.background = pygame.image.load('Assets/Pictures/home_background.png')
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        self.run = True
        self.auth = Authentification()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def update(self,email):
        self.screen.blit(self.background, (0, 0))

        pygame.draw.rect(self.screen, self.beige, (50, 50,300,self.screen_height - 90), border_radius=30)
        pygame.draw.rect(self.screen, self.white, (70, 220,260,65), border_radius=30)
        pygame.draw.rect(self.screen, self.white, (70, 340,260,65), border_radius=30)
        pygame.draw.rect(self.screen, self.white, (70, 460,260,65), border_radius=30)
        pygame.draw.circle(self.screen, self.white, (110, 120), 40)

        messages_text_render = self.font_before.render("Messages", True, self.blue)
        messages_text_rect = messages_text_render.get_rect(topleft=(125, 235))
        self.screen.blit(messages_text_render, messages_text_rect)

        channels_text_render = self.font_before.render("Channels", True, self.blue)
        channels_text_rect = channels_text_render.get_rect(topleft=(128, 355))
        self.screen.blit(channels_text_render, channels_text_rect)


        user_info = self.auth.get_user_info(email)
        
        if user_info:
            username_text_render = self.font_before.render(f"{user_info['username']}", True, self.blue)
            username_text_rect = username_text_render.get_rect(topleft=(180, 100))
            self.screen.blit(username_text_render, username_text_rect)
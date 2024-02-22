import pygame

class BasePage():
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.grey="#5c5959"
        self.white="#ffffff"
        self.background = pygame.image.load('Data/Pictures/home_background.png')
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        self.run = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def update(self):
        self.screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.screen, self.grey, (50, 50,300,self.screen_height - 90), border_radius=30)
        pygame.draw.circle(self.screen, self.white, (110, 120), 40)
        pygame.display.update()


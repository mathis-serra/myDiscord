import pygame

#Class Button to be used for all events when a button is clicked and button creation

class Button():
    def __init__(self, text, position, text_offset, action, color, width=150, height=100):
        self.text = text
        self.position = position
        self.text_offset = text_offset
        self.action = action
        self.font = pygame.font.Font(None, 36)
        self.color = color
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)

    #Method for creating the button's rectangle and thus allowing it to be displayed
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.width, self.height))
        text = self.font.render(self.text, True, (0, 0, 0))
        text_position = (self.position[0] + self.text_offset[0], self.position[1] + self.text_offset[1])
        screen.blit(text, text_position)

    #Method for enabling an event to take place when the rectangle is clicked on
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.action()

import pygame
import sys

class Button():
    def __init__(self, text, position, text_offset, action, color):
        self.text = text
        self.position = position
        self.text_offset = text_offset
        self.action = action
        self.font = pygame.font.Font(None, 36)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], 150, 100))
        text = self.font.render(self.text, True, (0, 0, 0))
        text_position = (self.position[0] + self.text_offset[0], self.position[1] + self.text_offset[1])
        screen.blit(text, text_position)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_rect = pygame.Rect(self.position[0], self.position[1], 150, 50)
            if button_rect.collidepoint(mouse_pos):
                self.action()

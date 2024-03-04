import pygame
from homepage.Bouton import Button

class ChatPage:
    def __init__(self, screen, user_id):
        self.screen = screen
        self.user_id = user_id
        self.chat_messages = []
        self.input_box = pygame.Rect(50, 600, 700, 32)
        self.input_text = ''
        self.white = "#ffffff" 
        self.send_button = Button("Send", (770, 600), (0, 0), self.send_message, self.white, width=100, height=40) 

    def new_rect(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.input_box, 2)
        font = pygame.font.Font(None, 28)
        input_text_surface = font.render(self.input_text, True, (0, 0, 0))
        self.screen.blit(input_text_surface, (self.input_box.x + 5, self.input_box.y + 5))
        self.send_button.draw(self.screen)
        self.display_chat()
        pygame.display.update()


    def display_chat(self):
        font = pygame.font.Font(None, 28)
        chat_y = 200
        for message in self.chat_messages:
            message_text = font.render(message, True, (0, 0, 0))
            message_rect = message_text.get_rect(topleft=(50, chat_y))
            self.screen.blit(message_text, message_rect)
            chat_y += 40

        pygame.display.update()

    def send_message(self):
        print("Message sent:", self.input_text)
        self.chat_messages.append(self.input_text)
        self.input_text = ''


    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            elif event.key == pygame.K_RETURN:
                self.send_message()
            else:
                self.input_text += event.unicode

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.send_button.rect.collidepoint(event.pos):
                        self.send_button.handle_event(event)

                self.handle_event(event)

            self.screen.fill(("#a31212"))
            self.new_rect()
            pygame.display.flip()

        pygame.quit()

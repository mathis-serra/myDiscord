import pygame
from homepage.Bouton import Button
from server.settings import settings
import mysql.connector
from datetime import datetime

class ChatPage:
    def __init__(self, screen, user_id, current_user_email):
        self.screen = screen
        self.user_id = user_id
        self.current_user_username = self.get_username_from_email(user_id)
        self.current_user_email = current_user_email
        self.current_user_friend = self.get_username_from_id(current_user_email)
        self.chat_messages = []
        self.input_box = pygame.Rect(50, 600, 700, 32)
        self.input_text = ''
        self.white = "#ffffff" 
        self.send_button = Button("Send", (770, 600), (0, 0), self.send_message, self.white, width=100, height=40) 
        self.background_image = pygame.image.load("Assets/Pictures/home_background.png")
        self.background_image = pygame.transform.scale(self.background_image, (1200, 700))
        self.font = pygame.font.Font(None, 35)

    def get_username_from_id(self, id):
        try:
            sql = "SELECT username FROM users WHERE id = %s"
            settings.cursor.execute(sql, (id,))
            user = settings.cursor.fetchone()
            if user:
                return user[0]
        except mysql.connector.Error as err:
            print("Erreur lors de la récupération de l'username de l'utilisateur:", err)
        return ""
    
    def get_username_from_email(self, email):
        try:
            sql = "SELECT username FROM users WHERE email = %s"
            settings.cursor.execute(sql, (email,))
            user = settings.cursor.fetchone()
            if user:
                return user[0]
        except mysql.connector.Error as err:
            print("Erreur lors de la récupération de l'username de l'utilisateur:", err)
        return ""

    def new_rect(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.input_box, 2)
        input_text_surface = self.font.render(self.input_text, True, (self.white))
        self.screen.blit(input_text_surface, (self.input_box.x + 5, self.input_box.y + 5))
        pygame.draw.rect(self.screen, ("#5c5959"), pygame.Rect(900, 0, 300, 1200))
        current_user_text = self.font.render(self.current_user_username, True, (self.white))
        self.screen.blit(current_user_text, (960, 10))
        other_user_text = self.font.render(self.current_user_friend, True, (self.white))
        self.screen.blit(other_user_text, (960, 80))
        pygame.draw.circle(self.screen, (255, 255, 255), (930, 30), 20)
        pygame.draw.circle(self.screen, (255, 255, 255), (930, 100), 20)
        self.send_button.draw(self.screen)
        self.display_chat()
        pygame.display.update()

    def display_chat(self):
        chat_y = 50
        for message in self.chat_messages:
            message_text = self.font.render(message, True, (self.white))
            message_rect = message_text.get_rect(topleft=(70, chat_y))
            pygame.draw.circle(self.screen, (255, 255, 255), (30, chat_y + message_rect.height // 2), 20)
            self.screen.blit(message_text, message_rect)
            chat_y += 70

        pygame.display.update()

    def send_message(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        message = f"{self.current_user_username} à {current_time} \n{self.input_text}"
        print("Message sent:", message)
        self.chat_messages.append(message)
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

            self.screen.blit(self.background_image, (0, 0))
            self.new_rect()
            pygame.display.flip()

        pygame.quit()

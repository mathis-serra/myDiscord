import pygame
from homepage.BasepageInterface import BasePage
from homepage.settings import settings
import mysql
from homepage.Chat_window import ChatWindow

class Messages(BasePage):
    def __init__(self, screen):
        super().__init__(screen)

    def new_rect(self):
        pygame.draw.rect(self.screen, self.beige, (430, 50, 700, self.screen_height - 90), border_radius=30)
        self.display_users()
        pygame.display.update()

    def display_users(self):
        try:
            sql = "SELECT username FROM users"
            settings.cursor.execute(sql)
            users = settings.cursor.fetchall()

            x_position = 450
            y_position = 100
            font = pygame.font.Font(None, 36)
            user_count = len(users)
            max_users_per_column = 11
            users_displayed = 0

            for user in users:
                email = user[0]
                user_text = font.render(email, True, (0, 0, 0))
                user_rect = user_text.get_rect(topleft=(x_position, y_position))
                self.screen.blit(user_text, user_rect)
                y_position += 50
                users_displayed += 1

                if user_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.connect_to_user(email)  # Connectez-vous à l'utilisateur sélectionné

                if users_displayed % max_users_per_column == 0:
                    y_position = 100
                    x_position += 100

            pygame.display.update()

        except mysql.connector.Error as err:
            print("Erreur lors de la récupération et de l'affichage des utilisateurs:", err)

    def connect_to_user(self, target_user):
        chat_window = ChatWindow(self.screen, target_user)
        chat_window.run()


        

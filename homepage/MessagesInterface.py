import pygame
from homepage.BasepageInterface import BasePage
from server.settings import settings
import mysql
from homepage.Bouton import Button

class Messages(BasePage):
    def __init__(self, screen):
        super().__init__(screen)
        self.buttons = []

    def new_rect(self):
        pygame.draw.rect(self.screen, self.beige, (430, 50, 700, self.screen_height - 90), border_radius=30)
        self.display_users()
        pygame.display.update()

    def display_users(self):
        try:
            sql = "SELECT id, username FROM users"
            settings.cursor.execute(sql)
            users = settings.cursor.fetchall()

            x_position = 450
            y_position = 100
            font = pygame.font.Font(None, 36)
            max_users_per_column = 11
            users_displayed = 0

            for user in users:
                user_id, username = user[0], user[1]
                user_text = font.render(username, True, (0, 0, 0))
                user_rect = user_text.get_rect(topleft=(x_position, y_position))
                self.screen.blit(user_text, user_rect)

                button = Button("Show Info", (x_position, y_position-20), (0, 0), lambda u_id=user_id, u_name=username: self.print_user_info(u_id, u_name), (255, 255, 255),width=100, height=50)
                self.buttons.append(button)

                y_position += 100
                users_displayed += 1

                if users_displayed % max_users_per_column == 0:
                    y_position = 100
                    x_position += 200

        except mysql.connector.Error as err:
            print("Erreur lors de la récupération et de l'affichage des utilisateurs:", err)

    def draw_buttons(self):
        for button in self.buttons:
            button.draw(self.screen)

    def print_user_info(self, user_id, username):
        # Affiche les informations de l'utilisateur lorsque le bouton est cliqué
        print("Informations de l'utilisateur :")
        print("User ID:", user_id)
        print("Username:", username)

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

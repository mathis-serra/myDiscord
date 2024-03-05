import pygame
from homepage.BasepageInterface import BasePage
import server.settings as settings
import mysql
from homepage.Bouton import Button
from homepage.Chat import ChatPage

class Messages(BasePage):
    def __init__(self, screen, current_user_email):
        super().__init__(screen)
        self.current_user_email = current_user_email
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

                # Utilisez la classe ChatPage pour créer une nouvelle page de chat lorsque le bouton est cliqué
                button = Button("Start Chat", (x_position, y_position-20), (0, 0), lambda u_id=user_id: self.create_chat(u_id), (255, 255, 255),width=100, height=50)
                self.buttons.append(button)

                y_position += 100
                users_displayed += 1

                if users_displayed % max_users_per_column == 0:
                    y_position = 100
                    x_position += 200

        except mysql.connector.Error as err:
            print("Erreur lors de la récupération et de l'affichage des utilisateurs:", err)

    def close(self):
        pygame.quit()

    def create_chat(self, other_user_id):
        print("Chat started with user ID:", other_user_id)
        chat_page = ChatPage(self.screen, self.current_user_email, other_user_id) 
        chat_page.run()
        self.close()

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

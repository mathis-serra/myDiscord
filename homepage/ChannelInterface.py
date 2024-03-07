import pygame
from homepage.BasepageInterface import BasePage
from server.settings import settings
import mysql
from homepage.Bouton import Button
from homepage.ChatChannel import ChatChannel

#Child of the BasePage class, which creates a rectangle and selects the users to send a message to. 
class MessagesChannels(BasePage):
    def __init__(self, screen, current_user_email):
        super().__init__(screen)
        self.current_user_email = current_user_email
        self.buttons = []

    #Method to create a rectangle and place all useful elements inside it
    def new_rect(self):
        pygame.draw.rect(self.screen, self.beige, (430, 50, 700, self.screen_height - 90), border_radius=30)
        self.display_channels()
        pygame.display.update()

    #Method for displaying all database users in the rectangle and allowing them to be selected
    def display_channels(self):
        try:
            sql = "SELECT id, name FROM channels"
            settings.cursor.execute(sql)
            channels = settings.cursor.fetchall()

            x_position = 450
            y_position = 100
            font = pygame.font.Font(None, 36)
            max_channels_per_column = 11
            channels_displayed = 0

            for channel in channels:
                channel_id, name = channel[0], channel[1]
                channel_text = font.render(name, True, (0, 0, 0))
                channel_rect = channel_text.get_rect(topleft=(x_position, y_position))
                self.screen.blit(channel_text, channel_rect)

                #Use the ChatPage class to create a new chat page when the button is clicked
                button = Button("Start Chat", (x_position, y_position-20), (0, 0), lambda u_id=channel_id: self.create_tchat(u_id), (255, 255, 255),width=100, height=50)
                self.buttons.append(button)

                y_position += 100
                channels_displayed += 1

                if channels_displayed % max_channels_per_column == 0:
                    y_position = 100
                    x_position += 200

        except mysql.connector.Error as err:
            print("Erreur lors de la récupération et de l'affichage des channels:", err)
            

    #Method just for closing the window
    def close(self):
        pygame.quit()

    def get_id_from_email(self, email):
        try:
            sql = "SELECT id FROM users WHERE email = %s"
            settings.cursor.execute(sql, (email,))
            user = settings.cursor.fetchone()
            if user:
                return user[0]
        except mysql.connector.Error as err:
            print("Erreur lors de la récupération de l'username de l'utilisateur:", err)
        return ""

    def create_tchat(self, channel_id):
        print("Chat started by",self.current_user_email,"id ;",self.current_user_email,"channel id",channel_id)
        chat_channel = ChatChannel(self.screen, self.get_id_from_email(self.current_user_email), channel_id)
        chat_channel.run()

    #Method to make all users display a functional button
    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

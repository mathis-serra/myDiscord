import pygame
from homepage.Bouton import Button
from server.settings import settings
import mysql.connector
from datetime import datetime

class ChatChannel():
    def __init__(self, screen, user_id, channel_id):
        self.screen = screen
        self.user_id = user_id
        self.current_user_username = self.get_username_from_id(user_id)
        self.channel_id = channel_id
        self.channel_users = self.get_channel_users(channel_id)
        self.chat_messages = []
        self.input_box = pygame.Rect(50, 600, 700, 32)
        self.input_text = ''
        self.white = "#ffffff" 
        self.send_button = Button("Send", (770, 600), (0, 0), self.send_message, self.white, width=100, height=40) 
        self.background_image = pygame.image.load("Assets/Pictures/home_background.png")
        self.background_image = pygame.transform.scale(self.background_image, (1200, 700))
        self.font = pygame.font.Font(None, 35)
        self.load_messages()
        self.join_channel(user_id,channel_id)

    def load_messages(self):
        try:
            sql = "SELECT content FROM messages WHERE channel_id = %s ORDER BY created_at"
            settings.cursor.execute(sql, (self.channel_id,))
            messages = settings.cursor.fetchall()
            self.chat_messages = [message[0] for message in messages]
        except mysql.connector.Error as err:
            print("Error loading messages from database:", err)

    def insert_message(self, message):
        try:
            sql = "INSERT INTO messages (user_id, channel_id, content, created_at) VALUES (%s, %s, %s, %s)"
            values = (self.user_id, self.channel_id, message, datetime.now())
            settings.cursor.execute(sql, values)
            settings.db.commit()
            print("Message inserted into database:", message)
        except mysql.connector.Error as err:
            print("Error inserting message into database:", err)

    def join_channel(self, user_id, channel_id):
        try:
            # Vérifiez d'abord si l'utilisateur est déjà dans le canal
            sql_check = "SELECT COUNT(*) FROM user_channel WHERE user_id = %s AND channel_id = %s"
            values_check = (user_id, channel_id)
            settings.cursor.execute(sql_check, values_check)
            result = settings.cursor.fetchone()
            if result[0] == 0:
                sql_insert = "INSERT INTO user_channel (user_id, channel_id) VALUES (%s, %s)"
                values_insert = (user_id, channel_id)
                settings.cursor.execute(sql_insert, values_insert)
                settings.db.commit()
                print("L'utilisateur a été ajouté au canal avec succès.")
            else:
                print("L'utilisateur est déjà dans le canal.")
        except mysql.connector.Error as err:
            print("Erreur lors de l'insertion de l'utilisateur dans le canal :", err)

    #Method to retrieve username by id 
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
    
    def get_channel_users(self, channel_id):
        try:
            sql = "SELECT user_id FROM user_channel WHERE channel_id = %s"
            settings.cursor.execute(sql, (channel_id,))
            users = settings.cursor.fetchall()
            return [user[0] for user in users]
        except mysql.connector.Error as err:
            print("Error loading channel users from database:", err)
            return []
      
    #Method to retrieve username by email
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
    
    def display_users(self):
        try:
            users = self.channel_users
            y_position = 10
            font = pygame.font.Font(None, 30)

            for user_id in users:
                username = self.get_username_from_id(user_id)
                user_text = font.render(username, True, (255, 255, 255))
                pygame.draw.circle(self.screen, (255, 255, 255), (930, y_position+20), 20)
                self.screen.blit(user_text, (960, y_position))
                y_position += 70 
        except mysql.connector.Error as err:
            print("Erreur lors de l'affichage des utilisateurs du canal :", err)

    #Method for displaying all page elements useful for using chat
    def new_rect(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.input_box, 2)
        input_text_surface = self.font.render(self.input_text, True, (self.white))
        self.screen.blit(input_text_surface, (self.input_box.x + 5, self.input_box.y + 5))
        pygame.draw.rect(self.screen, ("#5c5959"), pygame.Rect(900, 0, 300, 1200))
        self.send_button.draw(self.screen)
        self.display_users()
        self.display_chat()
        pygame.display.update()

    

    #Method for displaying messages on the interface
    def display_chat(self):
        chat_y = 50
        for message in self.chat_messages:
            message_text = self.font.render(message, True, (self.white))
            message_rect = message_text.get_rect(topleft=(70, chat_y))
            pygame.draw.circle(self.screen, (255, 255, 255), (30, chat_y + message_rect.height // 2), 20)
            self.screen.blit(message_text, message_rect)
            chat_y += 70

        pygame.display.update()

    #Method for sending the message as a string
    def send_message(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        message = f"{self.current_user_username} à {current_time} \n{self.input_text}"
        print("Message sent:", message)
        self.insert_message(message)
        self.chat_messages.append(message)
        self.input_text = ''

    #Method for making keyboard events
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            elif event.key == pygame.K_RETURN:
                self.send_message()
            else:
                self.input_text += event.unicode

    #Method for starting the page and displaying all elements and functions
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
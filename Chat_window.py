# import pygame
# from server.sockets_client import Client
# from server.sockets_server import Server

# class ChatWindow:
#     def __init__(self, screen, target_user):
#         self.screen = screen
#         self.target_user = target_user
#         self.chat_client = Client()  # Initialisez le client de chat
#         self.chat_server = Server()  # Initialisez le serveur de chat
#         self.chat_server.receive()  # Lancez le serveur de chat
#         self.chat_client.connect_to_server()  # Connectez-vous au serveur de chat
#         self.chat_client.send_message(f"/connect {target_user}")  # Envoyez un message pour initier la connexion
#         self.running = True
#         self.input_box = pygame.Rect(100, 550, 540, 40)
#         self.input_text = ''



#     # La logique pour gérer les événements, envoyer des messages, et dessiner la fenêtre de chat reste inchangée


#     def run(self):
#         while self.running:
#             self.handle_events()
#             self.draw()

#     def handle_events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.running = False
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN:
#                     self.send_message()
#                 elif event.key == pygame.K_BACKSPACE:
#                     self.input_text = self.input_text[:-1]
#                 else:
#                     self.input_text += event.unicode

#     def send_message(self):
#         if self.input_text.strip():  # Vérifiez si le message n'est pas vide
#             self.chat_client.send_message(self.input_text, self.target_user)
#             self.input_text = ''

#     def draw(self):
#         self.screen.fill((255, 255, 255))
#         pygame.draw.rect(self.screen, (0, 0, 0), self.input_box, 2)
#         font = pygame.font.Font(None, 32)
#         text_surface = font.render(self.input_text, True, (0, 0, 0))
#         self.screen.blit(text_surface, (self.input_box.x + 5, self.input_box.y + 5))
#         pygame.display.flip()
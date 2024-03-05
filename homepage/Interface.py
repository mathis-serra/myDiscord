import pygame
import server.settings as settings
from homepage.BasepageInterface import BasePage
from homepage.MessagesInterface import Messages
from homepage.Bouton import Button
from homepage.Change_profile import Profil
from server.sockets_server import Serveur
class Interface():
    def main(self, email):
        pygame.init()
        pygame.mixer.init()

        # Create an instance of the Server class
        server = Server()

        # Start the server
        server.start_server()



        # Fenetre
        screen_height = 700
        screen_width = 1200
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Sficord')

        # Define a function to change the state of the pages
        def switch_to_profil():

            nonlocal profil_page_run,message_page_run,message_user_run

            profil_page_run = True
            message_page_run = False
            message_user_run = False

        def switch_to_messages():
            nonlocal profil_page_run,message_page_run,message_user_run
            profil_page_run = False
            message_page_run = True
            message_user_run = False
            Serveur.serveur_main()

            

        blue = "#1769aa"

        # Create the buttons
        profil_button = Button("Profil", (70, 80), (36, 15), switch_to_profil, blue, width=90, height=80)
        messages_button = Button("Messages", (70, 220), (36, 15), switch_to_messages, blue, width=260, height=65)
        channels_button = Button("Channels", (70, 340), (36, 15), switch_to_messages, blue, width=260, height=65)

        # Initialize the pages
        base_page = BasePage(screen)
        profile_page = Profil(screen)
        message_page = Messages(screen,email)

        # Variables de contrôle pour l'affichage des pages
        run = True
        profil_page_run = False
        message_page_run = False
        message_user_run = False

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                profil_button.handle_event(event)
                messages_button.handle_event(event)
                channels_button.handle_event(event)

            
            screen.fill((0,0,0))

            base_page.update(email)

            if profil_page_run:
                profile_page.new_rect()

            if message_page_run:
                message_page.new_rect()
                message_page.handle_event(event)
                message_user_run = False



            pygame.display.flip()

        pygame.quit()

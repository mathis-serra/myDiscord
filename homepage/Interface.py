import datetime
import socket
import threading
import server.settings as settings
import time 

host = socket.gethostname()
port = 5001

clients = []
nicknames = []

def send_message(content, user_id, channel_id):
    sql = "INSERT INTO messages (user_id, channel_id, content, created_at, modified_at) VALUES (%s, %s, %s, %s, %s)"
    val = (user_id, channel_id, content, datetime.datetime.now(), datetime.datetime.now())
    settings.cursor.execute(sql, val)
    settings.db.commit()
    print(settings.cursor.rowcount, "record(s) inserted", datetime.datetime.now())

def broadcast(message, sender_client):
    sender_index = clients.index(sender_client)
    sender_nickname = nicknames[sender_index]
    message_with_nickname = f"{sender_nickname}: {message.decode('utf-8')}"

    # Insert message into the database
    send_message(message, 1, 1)

    for client in clients:
        if client != sender_client:  # Exclude the sender client
            client.send(message_with_nickname.encode())

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if message.decode('utf-8').lower() == "bye":
                close_server()
                break
            broadcast(message, client)  # Broadcast the message to other clients
        except Exception as e:
            print("An error occurred:", str(e))
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'), client)
            nicknames.remove(nickname)
            break

def receive():
    global server
    server = socket.socket()
    server.bind((host, port))
    server.listen(2)
    print("Server is listening...")

    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'), client)
        client.send('Connected to server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

def close_server():
    for client in clients:
        client.send("Server is closing...".encode())
        client.close()
    server.close()
    print("Server closed.")

import pygame
from homepage.BasepageInterface import BasePage
from homepage.MessagesInterface import Messages
from Bouton import Button
from homepage.Change_profile import Profil

class Interface():
    def main(email):
        pygame.init()
        pygame.mixer.init()

        # Start the server
        receive_thread = threading.Thread(target=receive)
        receive_thread.start()

        # Fenetre
        screen_height = 700
        screen_width = 1200
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Sficord')

        # Define a function to change the state of the pages
        def switch_to_profil():
            nonlocal profil_page_run, message_page_run
            profil_page_run = True
            message_page_run = False

        def switch_to_messages():
            nonlocal profil_page_run, message_page_run
            profil_page_run = False
            message_page_run = True

        # Define the colors
        blue = "#1769aa"

        # Create the buttons
        profil_button = Button("Profil", (70, 80), (36, 15), switch_to_profil, blue, width=90, height=80)
        messages_button = Button("Messages", (70, 220), (36, 15), switch_to_messages, blue, width=260, height=65)
        channels_button = Button("Channels", (70, 340), (36, 15), switch_to_messages, blue, width=260, height=65)

        # Initialize the pages
        base_page = BasePage(screen)
        profile_page = Profil(screen)
        message_page = Messages(screen)

        # Variables de contrôle pour l'affichage des pages
        run = True
        profil_page_run = False
        message_page_run = False

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                profil_button.handle_event(event)
                messages_button.handle_event(event)
                channels_button.handle_event(event)

            screen.fill((0, 0, 0))
            base_page.update(email)

            if profil_page_run:
                profile_page.new_rect()

            if message_page_run:
                message_page.new_rect()

            # Draw buttons after updating pages
            profil_button.draw(screen)
            messages_button.draw(screen)
            channels_button.draw(screen)

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    Interface.main("test@example.com")

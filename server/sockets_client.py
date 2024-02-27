import socket
import threading
import mysql.connector
from homepage.settings import settings



def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            print(data)
        except Exception as e:
            print("An error occurred:", str(e))
            break

def start_chat():
    host = socket.gethostname()
    port = 5001

    client_socket = socket.socket()
    client_socket.connect((host, port))

     # Authentification de l'utilisateur
    email = input("Enter your username: ")
    password_hash = input("Enter your password: ")

    # Vérification des informations d'authentification dans la base de donnéesa
    settings.cursor.execute("SELECT name FROM users WHERE email = %s AND password_hash = %s", (email, password_hash))
    result = settings.cursor.fetchone()

    if result is None:
        print("Invalid username or password")
        return

    nickname = result[0]
    print("Welcome,", nickname)
    client_socket.send(nickname.encode())

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        client_socket.send(message.encode())

if __name__ == "__main__":
    start_chat()

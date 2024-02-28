import socket
import threading
import mysql.connector
from settings import settings
from Login_Inscription import Authentification

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            print(data)
        except Exception as e:
            print("An error occurred:", str(e))
            break

def start_chat(email, password_hash):
    host = socket.gethostname()
    port = 5001

    client_socket = socket.socket()
    client_socket.connect((host, port))

    # Vérification des informations d'authentification dans la base de données
    auth = Authentification()
    login_result = auth.login(email, password_hash)
    if not login_result["success"]:
        print(login_result["message"])
        return

    nickname = login_result["username"]
    print("Welcome,", nickname)
    client_socket.send(nickname.encode())

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        client_socket.send(message.encode())

if __name__ == "__main__":
    email = input("Enter your email: ")
    password_hash = input("Enter your password: ")
    start_chat(email, password_hash)

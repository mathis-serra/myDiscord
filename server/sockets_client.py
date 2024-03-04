import socket
import threading
from Login_Inscription import Authentification

class Client:
    def __init__(self, email, password_hash):
        self.email = email
        self.password_hash = password_hash

    def receive_messages(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                print(data)
            except Exception as e:
                print("An error occurred:", str(e))
                break

    def start_chat(self):
        host = socket.gethostname()
        port = 5001

        with socket.socket() as client_socket:
            client_socket.connect((host, port))

            auth = Authentification()
            login_result = auth.login(self.email, self.password_hash)
            if not login_result["success"]:
                print(login_result["message"])
                return

            nickname = login_result["username"]
            print("Welcome,", nickname)
            client_socket.send(nickname.encode())

            receive_thread = threading.Thread(target=self.receive_messages, args=(client_socket,))
            receive_thread.start()

            input_thread = threading.Thread(target=self.input_loop, args=(client_socket,))
            input_thread.start()

            receive_thread.join()
            input_thread.join()

    def input_loop(self, client_socket):
        while True:
            message = input()
            if not message:
                break
            client_socket.send(message.encode())

if __name__ == "__main__":
    email = input("Enter your email: ")
    password_hash = input("Enter your password: ")
    client = Client(email, password_hash)
    client.start_chat()

import socket
import threading
from Login_Inscription import Authentification  # Import the Authentification class
import Chat as ChatPage  # Import the ChatPage class

class Client:
    def __init__(self):
        pass

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

    def start_chat(self, email, password):
        host = socket.gethostname()
        port = 5001

        with socket.socket() as client_socket:
            client_socket.connect((host, port))

            auth = Authentification()
            login_result = auth.login(email, password)
            if not login_result["success"]:
                print(login_result["message"])
                return

            nickname = login_result.get("username")
            if nickname is None:
                nickname = " "
            print("Welcome,", nickname)
            client_socket.send(nickname.encode())

            receive_thread = threading.Thread(target=self.receive_messages, args=(client_socket,))
            receive_thread.start()

            input_thread = threading.Thread(target=self.input_loop, args=(client_socket,))
            input_thread.start()

            # Create and run the ChatPage
            chat_page = ChatPage.ChatPage(client_socket, 7, "b")
            chat_page.run()

    def input_loop(self, client_socket):
        while True:
            message = input()
            if not message:
                break
            client_socket.send(message.encode())

if __name__ == "__main__":
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    client = Client()
    client.start_chat(email, password)

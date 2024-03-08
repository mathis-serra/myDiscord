import datetime
import socket
import threading
from settings import settings


class Server:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 5001
        self.server_socket = socket.socket()
        self.clients = {}
        self.nicknames = {}
#start the server in the host on port 5001
    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(2)
        print("Server is listening...")
#send the message to the client 
    def send_message(self, content, recipient):
        recipient.send(content.encode())
#display the messages to all clients 
    def broadcast(self, message, sender_nickname):
        for nickname, client_socket in self.clients.items():
            if nickname != sender_nickname:
                self.send_message(message, client_socket)
#handle the connexion from the client 
    def handle_client(self, client_socket, nickname):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    self.broadcast(f"{nickname}: {message}", nickname)
            except Exception as e:
                print("An error occurred:", str(e))
                break
# accept the connnexion if the username and password are True 
    def accept_clients(self):
        while True:
            client_socket, address = self.server_socket.accept()
            print("Connected with {}".format(str(address)))

            nickname = client_socket.recv(1024).decode('ascii')
            self.nicknames[client_socket] = nickname
            self.clients[nickname] = client_socket

            print("Nickname is {}".format(nickname))
            client_socket.send('Connected to server!'.encode('ascii'))

            thread = threading.Thread(target=self.handle_client, args=(client_socket, nickname))
            thread.start()
# close the server 
    def close_server(self):
        for client_socket in self.clients.values():
            client_socket.send("Server is closing...".encode())
            client_socket.close()
        self.server_socket.close()
        print("Server closed.")

if __name__ == "__main__":
    server = Server()
    server.start_server()
    server.accept_clients()

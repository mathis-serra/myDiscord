import datetime
import socket
import threading
<<<<<<< HEAD
import settings as settings


class Server:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 5001
        self.server_socket = socket.socket()
        self.clients = {}
        self.nicknames = {}

    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(2)
        print("Server is listening...")

    def send_message(self, content, recipient):
        recipient.send(content.encode())

    def broadcast(self, message, sender_nickname):
        for nickname, client_socket in self.clients.items():
            if nickname != sender_nickname:
                self.send_message(message, client_socket)

    def handle_client(self, client_socket, nickname):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    self.broadcast(f"{nickname}: {message}", nickname)
            except Exception as e:
                print("An error occurred:", str(e))
                break

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
=======
import server.settings as settings
import time 


class Serveur():
    def serveur_main():
        host = socket.gethostname()
        port = 5001

        server = socket.socket()
        server.bind((host, port))
        server.listen(2)
        print("Server is listening...")

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


>>>>>>> server

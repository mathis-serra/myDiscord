import datetime
import socket
import threading
import server.settings as settings


<<<<<<< HEAD
class Server:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 5001
        self.server_socket = socket.socket()
        self.clients = []
        self.nicknames = []

    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(2)
        print("Server is listening...")

    def send_message(self, content, user_id, channel_id):
        sql = "INSERT INTO messages (user_id, channel_id, content, created_at, modified_at) VALUES (%s, %s, %s, %s, %s)"
        val = (user_id, channel_id, content, datetime.datetime.now(), datetime.datetime.now())
        settings.cursor.execute(sql, val)
        settings.db.commit()
        print(settings.cursor.rowcount, "record(s) inserted", datetime.datetime.now())

    def broadcast(self, message, sender_client):
        sender_index = self.clients.index(sender_client)
        sender_nickname = self.nicknames[sender_index]
        message_with_nickname = f"{sender_nickname}: {message.decode('utf-8')}"

        # Insert message into the database
        self.send_message(message, 1, 1)
=======
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
>>>>>>> server

        for client in self.clients:
            if client != sender_client:  # Exclude the sender client
                client.send(message_with_nickname.encode())

<<<<<<< HEAD
    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024)
                if message.decode('utf-8').lower() == "bye":
                    self.close_server()
                    break
                self.broadcast(message, client)  # Broadcast the message to other clients
            except Exception as e:
                print("An error occurred:", str(e))
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.broadcast(f'{nickname} left!'.encode('ascii'), client)
                self.nicknames.remove(nickname)
                break

    def accept_clients(self):
        while True:
            client, address = self.server_socket.accept()
            print("Connected with {}".format(str(address)))

            nickname = client.recv(1024).decode('ascii')
            self.nicknames.append(nickname)
            self.clients.append(client)

            print("Nickname is {}".format(nickname))
            self.broadcast("{} joined!".format(nickname).encode('ascii'), client)
            client.send('Connected to server!'.encode('ascii'))

            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

    def close_server(self):
        for client in self.clients:
            client.send("Server is closing...".encode())
            client.close()
        self.server_socket.close()
        print("Server closed.")

if __name__ == "__main__":
    server = Server()
    server.start_server()
    server.accept_clients()
=======

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

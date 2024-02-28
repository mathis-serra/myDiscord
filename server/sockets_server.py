import datetime
import socket
import threading
import server.settings as settings
import time 

class Server():
    def __init__(self):
        self.clients = []
        self.nicknames = []
    
    def server_main(self):
        host = socket.gethostname()
        port = 5001

        server = socket.socket()
        server.bind((host, port))
        server.listen(2)
        print("Server is listening...")

        def send_message(content, user_id, channel_id):
            sql = "INSERT INTO messages (user_id, channel_id, content, created_at, modified_at) VALUES (%s, %s, %s, %s, %s)"
            val = (user_id, channel_id, content, datetime.datetime.now(), datetime.datetime.now())
            settings.cursor.execute(sql, val)
            settings.db.commit()
            print(settings.cursor.rowcount, "record(s) inserted", datetime.datetime.now())

        def broadcast(message, sender_client):
            sender_index = self.clients.index(sender_client)
            sender_nickname = self.nicknames[sender_index]
            message_with_nickname = f"{sender_nickname}: {message.decode('utf-8')}"

            # Insert message into the database
            send_message(message, 1, 1)

            for client in self.clients:
                if client != sender_client:  # Exclude the sender client
                    client.send(message_with_nickname.encode())

        def handle(client):
            run = True
            while run:
                try:
                    message = client.recv(1024)
                    if message.decode('utf-8').lower() == "bye":
                        close_server()
                        break
                    broadcast(message, client)  # Broadcast the message to other clients
                except Exception as e:
                    print("An error occurred:", str(e))
                    index = self.clients.index(client)
                    self.clients.remove(client)
                    client.close()
                    nickname = self.nicknames[index]
                    broadcast('{} left!'.format(nickname).encode('ascii'), client)
                    self.nicknames.remove(nickname)
                    run = False
                    break

        def close_server():
            for client in self.clients:
                client.send("Server is closing...".encode())
                client.close()
            server.close()
            print("Server closed.")

        def receive():
            run = True
            while run:
                client, address = server.accept()
                print("Connected with {}".format(str(address)))

                nickname = client.recv(1024).decode('ascii')
                self.nicknames.append(nickname)
                self.clients.append(client)

                print("Nickname is {}".format(nickname))
                broadcast("{} joined!".format(nickname).encode('ascii'), client)
                client.send('Connected to server!'.encode('ascii'))

                thread = threading.Thread(target=handle, args=(client,))
                thread.start()
            else :
                run = False
            
       
        receive()
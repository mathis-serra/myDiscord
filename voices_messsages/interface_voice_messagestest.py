import tkinter as tk
from voice_chat import VoiceChatApp
from pydub import AudioSegment
from pydub.playback import play

class DiscordInterface(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.title("Discord - General Channel")
        self.geometry("1200x700")
        self.configure(bg="#7442d7")  # Couleur violet foncé

        # Ajout des boîtes pour les canaux textuels
        text_channels_labels = ["Général", "Annonces", "Privé 1", "Privé 2"]
        self.create_channel_box(text_channels_labels, "Canaux Textuels", 0, 0, 0.22, 1, "#603BAB")

        # Ajout de la barre en bas à droite
        bottom_bar = tk.Frame(self, bg="#2C2F33", bd=2, relief=tk.SOLID)
        bottom_bar.place(relx=0.8, rely=0.75, relwidth=0.2, relheight=0.2)

        # Ajout des boutons dans la barre
        record_button = tk.Button(bottom_bar, text="Record", command=self.start_recording, bg="#555555", fg="white")
        record_button.pack(side="left", padx=5)

        stop_button = tk.Button(bottom_bar, text="Stop", command=self.stop_recording, bg="#555555", fg="white")
        stop_button.pack(side="left", padx=5)

        play_button = tk.Button(bottom_bar, text="Play", command=self.play_recorded_audio, bg="#555555", fg="white")
        play_button.pack(side="left", padx=5)

        send_button = tk.Button(bottom_bar, text="Send", command=self.send_audio_to_user, bg="#555555", fg="white")
        send_button.pack(side="left", padx=5)

        # Ajout d'une boîte pour entrer les messages
        self.message_entry = tk.Entry(self, bg="#CCCCCC", fg="#333333")
        self.message_entry.place(relx=0.22, rely=0.79, relwidth=0.35, relheight=0.06)

        # Ajout d'un bouton avec une flèche pour envoyer le message
        send_button = tk.Button(self, text="➔", command=self.send_message, font=("Arial", 16), bg="#555555", fg="white")
        send_button.place(relx=0.58, rely=0.79, relwidth=0.1, relheight=0.06)

        # Ajout d'un widget de texte pour afficher les messages
        self.message_display = tk.Text(self, bg="#333333", fg="#CCCCCC", wrap="word")
        self.message_display.place(relx=0.22, rely=0.1, relwidth=0.56, relheight=0.6)

        # Instance de VoiceChatApp avec une référence à l'interface
        self.voice_chat_app = VoiceChatApp(self)

    def create_channel_box(self, channel_labels, title, relx, rely, relwidth, relheight, box_bg):
        channel_box = tk.Frame(self, bg=box_bg, bd=2, relief=tk.SOLID)
        channel_box.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)

        # Ajoute des étiquettes pour les canaux 
        for channel_label in channel_labels:
            box = tk.Frame(channel_box, bg="black", bd=1, relief=tk.SOLID)  # Noir
            box.pack(side="top", fill="x", pady=2)

            label = tk.Label(box, text=channel_label, font=("Helvetica", 12), fg="white", bg="black")
            label.pack(side="top", fill="x", pady=5)

        # Ajoute le titre au-dessus des étiquettes
        title_label = tk.Label(channel_box, text=title, font=("Helvetica", 16, "bold"), fg="white", bg=box_bg)
        title_label.pack(side="top", fill="x", pady=5)

    def start_recording(self):
        # Utilisez threading pour exécuter l'enregistrement dans un thread séparé
        import threading
        recording_thread = threading.Thread(target=self.voice_chat_app.start_recording)
        recording_thread.start()

    def stop_recording(self):
        self.voice_chat_app.stop_recording()

    def on_recording_complete(self):
        # Cette méthode est appelée après l'enregistrement pour effectuer des opérations sur l'interface graphique

        print("Recording complete!")

    def play_recorded_audio(self):
        recorded_file = "recorded_audio.wav"  # Assurez-vous de mettre le bon chemin du fichier audio
        play(AudioSegment.from_wav(recorded_file))

    def send_audio_to_user(self):
        recorded_file = "recorded_audio.wav"
        self.voice_chat_app.send_audio_to_server(recorded_file)
        self.display_message("Audio envoyé au serveur avec succès!")

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.display_message(f"You: {message}")
            # Ajoutez ici la logique pour envoyer le message à la personne (par exemple, via un canal de chat)

    def display_message(self, message):
        # Affiche le message dans le widget de texte
        self.message_display.insert(tk.END, message + "\n")
        self.message_display.see(tk.END)  # Fait défiler vers le bas pour montrer le dernier message

    def display_audio_message(self, message):
        # Affiche le message audio dans le widget de texte
        self.display_message(message)

if __name__ == "__main__":
    app = DiscordInterface()
    app.mainloop()

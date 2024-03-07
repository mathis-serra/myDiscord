# voice_chat.py
import sounddevice as sd
import soundfile as sf
import socket
import threading

class VoiceChatApp:
    def __init__(self, interface):
        self.interface = interface
        self.server_address = ('192.168.1.1', 12345)  # A changer ca 

    def start_recording(self):
        recorded_file = self.record_audio()
        if recorded_file:
            self.interface.on_recording_complete()
            threading.Thread(target=self.send_audio_to_server, args=(recorded_file,)).start()

    def stop_recording(self):
        # Ajoutez ici la logique pour arrêter l'enregistrement
        pass

    def send_audio_to_server(self, filename):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(self.server_address)
                with open(filename, 'rb') as audio_file:
                    data = audio_file.read(1024)
                    while data:
                        s.sendall(data)
                        data = audio_file.read(1024)
            print("Audio envoyé au serveur avec succès!")
        except Exception as e:
            print(f"Erreur lors de l'envoi audio : {e}")

    def record_audio(self, filename="recorded_audio.wav", duration=5, samplerate=44100, channels=2):
        print("Enregistrement audio en cours. Appuyez sur Ctrl+C pour arrêter l'enregistrement.")

        try:
            with sd.InputStream(device=None, channels=channels, samplerate=samplerate) as stream:
                audio_data, _ = stream.read(int(samplerate * duration))
                sf.write(filename, audio_data, samplerate, format='wav')

            print(f"Enregistrement terminé. Fichier audio sauvegardé sous: {filename}")
            return filename

        except KeyboardInterrupt:
            print(f"\nEnregistrement interrompu. Fichier audio sauvegardé sous: {filename}")
            return None

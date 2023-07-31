import socket
import ssl

# Adresse IP et port du serveur
SERVER_ADDRESS = ('localhost', 12345)

# Créer un socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Créer le contexte SSL
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

# Activer les options de vérification des certificats serveur (optionnel)
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(cafile="chemin/vers/server.crt")

# Connecter le socket au serveur
ssl_socket = context.wrap_socket(udp_socket, server_hostname=SERVER_ADDRESS[0])
ssl_socket.connect(SERVER_ADDRESS)

# Envoyer des données au serveur
message = "Hello, serveur!"
ssl_socket.send(message.encode())

# Recevoir la réponse du serveur
data = ssl_socket.recv(1024)
print(f"Réponse du serveur: {data.decode()}")

# Fermer la connexion
ssl_socket.close()
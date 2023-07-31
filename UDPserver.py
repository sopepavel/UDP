import socket
import ssl

# Chemin vers le certificat et la clé privée auto-signés
CERTFILE = "chemin/vers/server.crt"
KEYFILE = "chemin/vers/server.key"

# Adresse IP et port du serveur
SERVER_ADDRESS = ('localhost', 12345)

# Créer un socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Créer le contexte SSL
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
(jls_ext)ract_var = context
jls_extract_var.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)

# Activer les options de vérification des certificats clients (optionnel)
context.verify_mode = ssl.CERT_OPTIONAL

# Associer le contexte SSL au socket UDP
ssl_socket = context.wrap_socket(udp_socket, server_side=True)

# Lier le socket à l'adresse du serveur
ssl_socket.bind(SERVER_ADDRESS)

print("Serveur démarré. En attente de connexions...")

while True:
    # Recevoir les données du client
    data, address = ssl_socket.recvfrom(1024)
    print(f"Reçu de {address}: {data.decode()}")

    # Répondre au client
    response = "Message bien reçu!"
    ssl_socket.sendto(response.encode(), address)
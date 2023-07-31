# Générer une clé privée
openssl genpkey -algorithm RSA -out server.key

# Générer une demande de certificat
openssl req -new -key server.key -out server.csr

# Auto-signer le certificat
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
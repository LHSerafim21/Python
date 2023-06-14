import socket

# Endereço IP e porta do servidor
SERVER_IP = socket.gethostname()
SERVER_PORT = 1234

# Cria o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao endereço IP e porta do servidor
server_socket.bind((SERVER_IP, SERVER_PORT))

# Define o limite máximo de conexões pendentes
server_socket.listen(1)
print('Aguardando conexão...')

# Aceita a conexão do cliente
client_socket, client_address = server_socket.accept()
print('Cliente conectado:', client_address)

# Recebe dados do cliente e envia uma resposta
while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print('Cliente:', data)
    response = 'Recebido: ' + data
    client_socket.send(response.encode())

# Encerra a conexão
client_socket.close()
server_socket.close()

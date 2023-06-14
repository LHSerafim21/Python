import socket

# Endereço IP e porta do servidor
SERVER_IP = socket.gethostname()
SERVER_PORT = 1234

# Cria o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
client_socket.connect((SERVER_IP, SERVER_PORT))

# Envia dados para o servidor e recebe a resposta
while True:
    message = input('Digite uma mensagem para o servidor: ')
    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    print('Servidor:', response)

    # Encerra a conexão se a mensagem for "sair"
    if message.lower() == 'sair':
        break

# Encerra a conexão
client_socket.close()

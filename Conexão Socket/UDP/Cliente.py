import socket

# Configuração do cliente
host = socket.gethostname()
port = 12345

# Cria um socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Loop para enviar pacotes
while True:
    # Solicita uma mensagem para o usuário
    message = input('Digite uma mensagem para enviar (ou "sair" para encerrar): ')

    if message.lower() == 'sair':
        break

    # Envia a mensagem para o servidor
    sock.sendto(message.encode(), (host, port))

    # Aguarda a resposta do servidor
    data, addr = sock.recvfrom(1024)

    # Imprime a resposta recebida
    print('Resposta do servidor:', data.decode())

# Fecha o socket
sock.close()

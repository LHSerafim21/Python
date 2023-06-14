import socket

# Endereço IP e porta do servidor
SERVER_IP = socket.gethostname()
SERVER_PORT_TCP = 1234
SERVER_PORT_UDP = 5678

# Cria o socket TCP do cliente
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.connect((SERVER_IP, SERVER_PORT_TCP))

# Cria o socket UDP do cliente
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Envia a escolha de protocolo para o servidor
protocol_choice = input('Digite "TCP" ou "UDP" para escolher o protocolo: ')
tcp_client_socket.send(protocol_choice.encode())

if protocol_choice.lower() == 'tcp':
    print('Cliente escolheu usar TCP')

    # Envia e recebe dados usando TCP
    while True:
        message = input('Digite uma mensagem para o servidor (ou "sair" para encerrar): ')
        tcp_client_socket.send(message.encode())

        if message.lower() == 'sair':
            break

        response = tcp_client_socket.recv(1024).decode()
        print('Servidor (TCP):', response)

elif protocol_choice.lower() == 'udp':
    print('Cliente escolheu usar UDP')

    # Envia e recebe dados usando UDP
    while True:
        message = input('Digite uma mensagem para o servidor (ou "sair" para encerrar): ')
        udp_client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT_UDP))

        if message.lower() == 'sair':
            break

        response, _ = udp_client_socket.recvfrom(1024)
        print('Servidor (UDP):', response.decode())

# Encerra as conexões
tcp_client_socket.close()
udp_client_socket.close()

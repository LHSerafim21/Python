import socket

# Endereço IP e porta do servidor
SERVER_IP = socket.gethostname()
SERVER_PORT_TCP = 1234
SERVER_PORT_UDP = 5678

# Cria o socket TCP do servidor
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind((SERVER_IP, SERVER_PORT_TCP))
tcp_server_socket.listen(1)
print('Servidor pronto para receber pacotes TCP...')

# Cria o socket UDP do servidor
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind((SERVER_IP, SERVER_PORT_UDP))
print('Servidor pronto para receber pacotes UDP...')

# Aceita a conexão TCP do cliente
tcp_client_socket, tcp_client_address = tcp_server_socket.accept()
print('Cliente TCP conectado:', tcp_client_address)

# Recebe e envia dados usando TCP ou UDP conforme escolha do usuário
while True:
    protocol_choice = tcp_client_socket.recv(1024).decode().lower()

    if protocol_choice == 'tcp':
        print('Cliente escolheu usar TCP')

        while True:
            data = tcp_client_socket.recv(1024).decode()
            if not data:
                break
            print('TCP:', data)
            response = 'Recebido via TCP: ' + data
            tcp_client_socket.send(response.encode())

            if data.lower() == 'sair':
                break

    elif protocol_choice == 'udp':
        print('Cliente escolheu usar UDP')

        while True:
            data, client_address = udp_server_socket.recvfrom(1024)
            if not data:
                break
            print('UDP:', data.decode())
            response = 'Recebido via UDP: ' + data.decode()
            udp_server_socket.sendto(response.encode(), client_address)

            if data.decode().lower() == 'sair':
                break

    else:
        break

# Encerra as conexões
tcp_client_socket.close()
tcp_server_socket.close()
udp_server_socket.close()

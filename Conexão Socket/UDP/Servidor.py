import socket

# Configuração do servidor
host = socket.gethostname()
port = 12345

# Cria um socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincula o socket ao endereço e porta
sock.bind((host, port))

print('Servidor pronto para receber pacotes.')

# Loop infinito para receber pacotes
while True:
    # Recebe o pacote e o endereço do cliente
    data, addr = sock.recvfrom(1024)

    # Imprime a mensagem recebida
    print('Mensagem recebida:', data.decode())

    # Envia uma resposta ao cliente
    response = 'Recebido com sucesso!'
    sock.sendto(response.encode(), addr)

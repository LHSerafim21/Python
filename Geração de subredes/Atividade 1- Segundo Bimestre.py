def calcular_subredes(ip, num_subredes):
    # Converte o endereço IP em uma lista de inteiros
    ip_parts = list(map(int, ip.split('.')))

    # Converte o número de subredes em um valor binário de 32 bits
    num_subredes_bits = bin(num_subredes)[2:].zfill(32)

    # Calcula o número de bits necessários para representar o número de subredes
    num_bits_subredes = num_subredes_bits.find('1')

    # Calcula o número de bits disponíveis para hosts em cada subrede
    num_bits_hosts = 32 - num_bits_subredes

    # Calcula o número de hosts disponíveis em cada subrede
    num_hosts_por_subrede = 2 ** num_bits_hosts - 2

    subredes = []
    endereco_rede = ip_parts[:]

    for i in range(num_subredes):
        # Calcula a máscara de subrede como uma lista de inteiros
        mascara_subrede = [0, 0, 0, 0]
        for j in range(num_bits_subredes):
            mascara_subrede[j // 8] |= 1 << (7 - j % 8)

        # Calcula o Broadcast
        broadcast = endereco_rede[:]
        for j in range(num_bits_hosts):
            broadcast[j // 8] |= 1 << (7 - j % 8)

        subredes.append({
            'ID de REDE': i + 1,
            'Endereço de Rede': '.'.join(map(str, endereco_rede)),
            'Broadcast': '.'.join(map(str, broadcast)),
            'Máscara de Rede': '.'.join(map(str, mascara_subrede)),
        })

        # Calcula o próximo endereço de rede
        endereco_rede[-1] += 2 ** num_bits_hosts
        for j in range(3, 0, -1):
            if endereco_rede[j] > 255:
                endereco_rede[j] -= 256
                endereco_rede[j - 1] += 1

    return subredes


if __name__ == '__main__':
    endereco_ip = input("Digite o endereço IPv4: ")
    numero_subredes = int(input("Digite o número de redes desejadas: "))

    subredes = calcular_subredes(endereco_ip, numero_subredes)

    for subrede in subredes:
        print("\nSubrede:")
        for chave, valor in subrede.items():
            print(f"{chave}: {valor}")

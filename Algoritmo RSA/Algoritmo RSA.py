# Import da biblioteca random para gerar números aleatórios e a função gcd do módulo math para calcular o máximo divisor comum.
import random
from math import gcd

def gerar_par_chaves():
    # Função que gera um número primo aleatório de aproximadamente n bits.
    def gerar_candidato_primo(comprimento):
        p = random.getrandbits(comprimento)
        p |= (1 << comprimento - 1) | 1  # Define o bit mais significativo e o menos significativo como 1.
        return p

    # Função que verifica se um número é primo usando o teste de Miller-Rabin.
    def e_primo(num, iteracoes=50):
        if num <= 3:
            return num == 2 or num == 3
        if num % 2 == 0:
            return False

        s, d = 0, num - 1
        while d % 2 == 0:
            s += 1
            d //= 2

        for _ in range(iteracoes):
            a = random.randrange(2, num - 1)
            x = pow(a, d, num)
            if x == 1 or x == num - 1:
                continue
            for _ in range(s - 1):
                x = pow(x, 2, num)
                if x == num - 1:
                    break
            else:
                return False
        return True

    # Função que encontra um número primo de aproximadamente n bits.
    def gerar_primo(comprimento=1024):
        while True:
            p = gerar_candidato_primo(comprimento)
            if e_primo(p):
                return p

    # Geramos dois números primos grandes.
    p = gerar_primo()
    q = gerar_primo()

    # Calculamos n, que será o módulo para ambas as chaves.
    n = p * q

    # Calculamos o totiente de Euler, φ(n).
    phi = (p - 1) * (q - 1)

    # Encontramos um número inteiro 'e' que seja co-primo a φ(n).
    # 'e' será o expoente da chave pública.
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Usamos o algoritmo estendido de Euclides para encontrar o inverso multiplicativo de 'e' modulo φ(n).
    # 'd' será o expoente da chave privada.
    d = pow(e, 1, phi)

    # Retornamos a chave pública (n, e) e a chave privada (n, d).
    return ((n, e), (n, d))

# Chamamos a função para gerar as chaves.
chave_publica, chave_privada = gerar_par_chaves()

# Exibimos as chaves para fins de demonstração.
print("Chave pública:", chave_publica)
print("Chave privada:", chave_privada)

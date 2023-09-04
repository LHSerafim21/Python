import hashlib

def cifra_cesar(texto, chave):
    resultado = ""
    for char in texto:
        if char.isalpha():
            ascii_code = ord(char)
            if char.islower():
                ascii_code = (ascii_code - 97 + chave) % 26 + 97
            else:
                ascii_code = (ascii_code - 65 + chave) % 26 + 65
            resultado += chr(ascii_code)
        else:
            resultado += char
    return resultado

def gerar_hash(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

def ler_chave_secreta():
    with open("chave_secreta.txt", "r") as arquivo:
        return int(arquivo.read())

def main():
    # Leitura da chave secreta
    chave_secreta = ler_chave_secreta()

    # Leitura do texto que deseja criptografar
    texto_original = input("Digite o texto que deseja criptografar: ")

    # Aplicação da técnica de substituição (Cifra de César)
    texto_cifrado = cifra_cesar(texto_original, chave_secreta)

    # Geração do hash do texto criptografado
    hash_resultante = gerar_hash(texto_cifrado)

    print("Texto original:", texto_original)
    print("Texto criptografado:", texto_cifrado)
    print("Hash resultante:", hash_resultante)

if __name__ == "__main__":
    main()

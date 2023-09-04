import heapq
import os

class Grafo:
    def __init__(self):
        self.vertices = {}  # Inicializa um dicionário vazio para armazenar os vértices e suas arestas com pesos.

    def adicionar_vertice(self, vertice):
        self.vertices[vertice] = {}  # Adiciona um novo vértice ao grafo sem arestas inicialmente.

    def adicionar_aresta(self, vertice1, vertice2, peso):
        self.vertices[vertice1][vertice2] = peso  # Adiciona uma aresta entre vertice1 e vertice2 com o peso informado.
        self.vertices[vertice2][vertice1] = peso  # Como é um grafo não direcionado, adiciona a mesma aresta no sentido inverso.

    def dijkstra(self, origem, destino):
        distancias = {vertice: float('inf') for vertice in self.vertices}
        # Inicializa todas as distâncias como infinito, exceto a origem, que terá distância zero.
        distancias[origem] = 0
        fila_prioridades = [(0, origem)]  # Cria uma fila de prioridades com a origem e sua distância inicial.
        caminho = {origem: None}  # Cria um dicionário para armazenar o caminho percorrido, com a origem sem nenhum caminho anterior.

        while fila_prioridades:
            distancia_atual, vertice_atual = heapq.heappop(fila_prioridades)
            # Obtém o vértice com menor distância (topo da fila de prioridades).

            if vertice_atual == destino:
                # Se o vértice atual é o destino, encerra o loop, pois encontramos o caminho mais curto.
                break

            for vertice_adjacente, peso in self.vertices[vertice_atual].items():
                nova_distancia = distancia_atual + peso
                # Calcula a nova distância a partir do vértice atual para os vértices adjacentes.

                if nova_distancia < distancias[vertice_adjacente]:
                    # Se a nova distância é menor que a distância atualmente armazenada, atualiza as informações.
                    distancias[vertice_adjacente] = nova_distancia
                    caminho[vertice_adjacente] = vertice_atual
                    # Armazena o vértice atual como o vértice anterior no caminho para vertice_adjacente.
                    heapq.heappush(fila_prioridades, (nova_distancia, vertice_adjacente))
                    # Adiciona o vértice_adjacente à fila de prioridades para ser processado posteriormente.

        caminho_percurso = [destino]  # Inicializa a lista para armazenar o caminho percorrido a partir do destino.
        vertice_atual = destino  # Começa pelo destino e vai retrocedendo no caminho até a origem.
        while caminho[vertice_atual] is not None:
            caminho_percurso.append(caminho[vertice_atual])
            # Adiciona o vértice anterior à lista do caminho.
            vertice_atual = caminho[vertice_atual]
            # Atualiza para o próximo vértice no caminho.

        caminho_percurso.reverse()
        # Inverte a lista para mostrar o caminho do início ao fim.

        return distancias[destino], caminho_percurso
        # Retorna a distância mínima e o caminho percorrido.


# Criando o grafo de exemplo
rede = Grafo()  # Cria uma instância da classe Grafo para representar a rede.

# Adicionando os vértices
vertices = ["A", "B", "C", "D", "E", "F"]
for vertice in vertices:
    rede.adicionar_vertice(vertice)
    # Adiciona os vértices "A", "B", "C", "D", "E" e "F" ao grafo.

# Solicitando ao usuário para adicionar as arestas
os.system("cls")
print("\nAdicione quantas arestas quiser com seus respectivos pesos. Para os Nos [A,B,C,D,E,F]")
print("         Digite 'sair' para finalizar o processo de adição de arestas.\n")
print("========================================================================================")
while True:
    vertice1 = input("Digite o primeiro vértice da aresta: ")
    if vertice1.lower() == "sair":
        break

    vertice2 = input("Digite o segundo vértice da aresta: ")
    peso = float(input("Digite o peso da aresta: "))
    os.system("cls")
    print("\nAdicione quantas arestas quiser com seus respectivos pesos. Para os Nos [A,B,C,D,E,F]")
    print("         Digite 'sair' para finalizar o processo de adição de arestas.\n")
    print("========================================================================================")
    rede.adicionar_aresta(vertice1, vertice2, peso)
    # Adiciona as arestas entre os vértices informados pelo usuário com os pesos fornecidos.

# Encontrando o caminho mais curto
origem = input("Digite o vértice de origem: ")  # Solicita ao usuário o vértice de origem para o caminho mais curto.
destino = input("Digite o vértice de destino: ")  # Solicita ao usuário o vértice de destino para o caminho mais curto.
distancia_minima, caminho_percurso = rede.dijkstra(origem, destino)
# Executa o algoritmo de Dijkstra no grafo para encontrar o caminho mais curto e a distância mínima.

# Imprimindo o resultado
print(f"Caminho mais curto de {origem} até {destino}:")
print(" --> ".join(caminho_percurso))
# Imprime o caminho percorrido, separando os vértices por setas.
print(f"Distância total percorrida: {distancia_minima}")
# Imprime a distância mínima percorrida no caminho mais curto.

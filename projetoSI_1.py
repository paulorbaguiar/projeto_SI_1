tempo_direto = [
    [0.0, 10.0, 18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1, 16.7, 27.3, 27.6, 29.8],
    [10.0, 0.0, 8.5, 14.8, 26.6, 29.1, 26.1, 17.3, 10.0, 3.5, 15.5, 20.9, 19.1, 21.8],
    [18.5, 8.5, 0.0, 6.3, 18.2, 20.6, 17.6, 13.6, 9.4, 10.3, 19.5, 19.1, 12.1, 16.6],
    [24.8, 14.8, 6.3, 0.0, 12.0, 14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4],
    [36.4, 26.6, 18.2, 12.0, 0.0, 3.0, 2.4, 19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9],
    [38.8, 29.1, 20.6, 14.4, 3.0, 0.0, 3.3, 22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2],
    [35.8, 26.1, 17.6, 11.5, 2.4, 3.3, 0.0, 20.0, 23.0, 27.3, 34.2, 25.7, 12.4, 15.6],
    [25.4, 17.3, 13.6, 12.4, 19.4, 22.3, 20.0, 0.0, 8.2, 20.3, 16.1, 6.4, 22.7, 27.6],
    [17.6, 10.0, 9.4, 12.6, 23.3, 25.7, 23.0, 8.2, 0.0, 13.5, 11.2, 10.9, 21.2, 26.6],
    [9.1, 3.5, 10.3, 16.7, 28.2, 30.3, 27., 20.3, 13.5, 0.0, 17.6, 24.2, 18.7, 21.2],
    [16.7, 15.5, 19.5, 23.6, 34.2, 36.7, 34.2, 16.1, 11.2, 17.6, 0.0, 14.2, 31.5, 35.5],
    [27.3, 20.9, 19.1, 18.6, 24.8, 27.6, 25.7, 6.4, 10.9, 24.2, 14.2, 0.0, 28.8, 33.6],
    [27.6, 19.1, 12.1, 10.6, 14.5, 15.2, 12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0.0, 5.1],
    [29.8, 21.8, 16.6, 15.4, 17.9, 18.2, 15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1, 0.0],
]


tempo_real = {
    1: [(2, "azul", 10)], 
    2: [(1, "azul", 10), (3, "azul", 8.5), (9, "amarela", 10), (10, "amarela", 3.5)],
    3: [(2, "azul", 8.5), (4, "azul", 6.3), (9, "vermelha", 9.4), (13, "vermelha", 18.7)],
    4: [(3, "azul", 6.3), (5, "azul",  13.0), (8, "verde", 15.3), (13, "verde", 12.8)],
    5: [(4, "azul",  13.0), (6, "azul", 3.0), (7, "amarela", 2.4), (8, "amarela", 30)],
    6: [(5, "azul",  3.0)],
    7: [(5, "amarela", 2.4)],
    8: [(4, "verde", 15.3), (5, "amarela", 30), (9, "amarela", 9.6), (12, "verde", 6.4)],
    9: [(2, "amarela", 10), (3, "vermelha", 9.4), (8, "amarela", 9.6), (11, "vermelha", 12.2)],
    10: [(2, "amarela", 3.5)],
    11: [(9, "vermelha", 12.2)],
    12: [(8, "verde", 6.4)],
    13: [(3, "vermelha", 18.7), (4, "verde", 12.8), (14, "verde", 5.1)],
    14: [(13, "verde", 5.1)]
    }

def vizinho(estado):
    if estado in tempo_real:
        return tempo_real[estado]

def a_estrela(origem, destino):

    fronteiras_abertas = []
    fronteiras_abertas.append(origem)

    fronteiras_fechadas = []

    g = {} # Custo real para chegar a cada estado
    pais = {} # Armazena o pai de cada estado no menor caminho

    g[origem] = 0
    pais[origem] = origem
    
    while len(fronteiras_abertas) != 0:

        estado_atual = 0

        for estado in fronteiras_abertas: # Encontrar o estado na fronteira aberta com o menor custo

            if estado_atual == 0:
                estado_atual = estado

            # Escolher o menor custo para definir o estado atual
            if g[estado] + tempo_direto[estado[0] - 1][destino[0] - 1] < g[estado_atual] + tempo_direto[estado_atual[0] - 1][destino[0] - 1]:
                estado_atual = estado
        
        if estado_atual != destino:

            for (numero, linha, distancia) in vizinho(estado_atual[0]):
                tupla = (numero, linha) # vizinhos do estado atual em formato de tupla

                if tupla not in fronteiras_abertas and tupla not in fronteiras_fechadas: # Adcionar tupla como fronteira não explorada

                    fronteiras_abertas.append(tupla)

                    print(f'Fronteira: {fronteiras_abertas}') 
                    
                    pais[tupla] = estado_atual # Definir o pai do vizinho como o estado atual
                    g[tupla] = g[estado_atual] + distancia # Atualizar o custo real para chegar ai vizinho
                    
                    # Adcionar baldeação se a linha mudar
                    if estado_atual[1] != tupla[1]:
                        g[tupla] = g[tupla] + 2 # 2 pois todo valor será dobrado no fim

                # Atualizar o custo se um caminho melhor for encontrado
                else:
                    if g[tupla] > g[estado_atual] + distancia:
                        g[tupla] = g[estado_atual] + distancia
                        pais[tupla] = estado_atual
                        if numero in fronteiras_fechadas:
                            fronteiras_fechadas.remove(tupla)
                            fronteiras_abertas.append(tupla)

        if (estado_atual == destino) or (estado_atual[0] == destino[0]):

            # Reconstruir o menor caminho
            menor_caminho = []
            while pais[estado_atual] != estado_atual:
                menor_caminho.append(estado_atual)
                estado_atual = pais[estado_atual]

            menor_caminho.append(origem)
            menor_caminho.reverse()

            # Adcionar a estação destino se a linha for diferente
            if (estado_atual[1] != destino[1]):
                menor_caminho.append(destino)
                if destino not in g:
                    g[destino] = g[menor_caminho[len(menor_caminho)-2]] + 2

            if menor_caminho[-2] == menor_caminho[-1]:
                menor_caminho.pop(-1) # Removendo duplicatas caso necessário

            print('O menor caminho até seu destino é ')
            for i in range(0, len(menor_caminho), 1):
                print(menor_caminho[i])
            print(f'Duração da viagem: {g[destino] * 2} minutos')       
            return menor_caminho

        fronteiras_abertas.remove(estado_atual)
        fronteiras_fechadas.append(estado_atual)


print("Por favor, insira a estação que você está: ")
origem = int(input())
print("Por favor, insira a cor da linha da estação que você está: ")
cor_origem = input()
print("Por favor, insira a estação destino: ")
destino = int(input())
print("Por favor, insira a cor da linha destino: ")
cor_destino = input()

a_estrela((origem, cor_origem), (destino, cor_destino))

#listas com distancia direta de estação até as demais (tabela 1)
est_dir_1 = [0.0, 10.0, 18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1, 16.7, 27.3, 27.6, 29.8]
est_dir_2 = [10.0, 0.0, 8.5, 14.8, 26.6, 29.1, 26.1, 17.3, 10.0, 3.5, 15.5, 20.9, 19.1, 21.8]
est_dir_3 = [18.5, 8.5, 0.0, 6.3, 18.2, 20.6, 17.6, 13.6, 9.4, 10.3, 19.5, 19.1, 12.1, 16.6]
est_dir_4 = [24.8, 14.8, 6.3, 0.0, 12.0, 14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4]
est_dir_5 = [36.4, 26.6, 18.2, 12.0, 0.0, 3.0, 2.4, 19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9]
est_dir_6 = [38.8, 29.1, 20.6, 14.4, 3.0, 0.0, 22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2]
est_dir_7 = [35.8, 26.1, 17.6, 11.5, 2.4, 3.3, 0.0, 20.0, 23.0, 27.3, 34.2, 25.7, 12.4, 15.6]
est_dir_8 = [25.4, 17.3, 13.6, 12.4, 19.4, 22.3, 20.0, 0.0, 8.2, 20.3, 16.1, 6.4, 22.7, 27.6]
est_dir_9 = [17.6, 10.0, 9.4, 12.6, 23.3, 25.7, 23.0, 8.2, 0.0, 13.5, 11.2, 10.9, 21.2, 26.6]
est_dir_10 = [9.1, 3.5, 10.3, 16.7, 28.2, 30.3, 27., 20.3, 13.5, 0.0, 17.6, 24.2, 18.7, 21.2]
est_dir_11 = [16.7, 15.5, 19.5, 23.6, 34.2, 36.7, 34.2, 16.1, 11.2, 17.6, 0.0, 14.2, 31.5, 35.5]
est_dir_12 = [27.3, 20.9, 19.1, 18.6, 24.8, 27.6, 25.7, 6.4, 10.9, 24.2, 14.2, 0.0, 28.8, 33.6]
est_dir_13 = [27.6, 19.1, 12.1, 10.6, 14.5, 15.2, 12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0.0, 5.1]
est_dir_14 = [29.8, 21.8, 16.6, 15.4, 17.9, 18.2, 15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1, 0.0]

distancias_diretas = [est_dir_1, est_dir_2, est_dir_3, est_dir_4, est_dir_5, est_dir_6, est_dir_7, est_dir_8, est_dir_9, est_dir_10, est_dir_11, est_dir_12, est_dir_13, est_dir_14]


#Dicionario contendo o número da estação linkado a uma lista de tuplas (num estação, cor linha, tempo real). (tabela 2)
distancias_reais = {1 : [(2, "azul", 10)], 
                    2 : [(1, "azul", 10), (3, "azul", 8.5), (10, "amarela", 3.5), (9, "amarela", 10)],
                    3 : [(2, "azul", 8.5), (4, "azul", 6.3), (9, "vermelha", 9.4), (13, "vermelha", 18.7)],
                    4 : [(3, "azul", 6.3), (5, "azul",  13.0), (8, "verde", 15.3), (13, "verde", 18.8)],
                    5 : [(4, "azul",  13.0), (6, "azul", 3.0), (7, "amarela", 2.4), (8, "amarela", 30)],
                    6 : [(5, "azul",  13.0)],
                    7 : [(5, "amarela", 2.4)],
                    8 : [(4, "verde", 15.3), (8, "amarela", 30), (9, "amarela", 9.6), (12, "verde", 6.4)],
                    9 : [(2, "amarela", 10), (3, "vermelha", 9.4), (8, "amarela", 9.6), (11, "vermelha", 12.2)],
                    10 : [(2, "amarela", 3.5)],
                    11 : [(11, "vermelha", 12.2)],
                    12 : [(12, "verde", 6.4)],
                    13 : [(13, "vermelha", 18.7), (13, "verde", 18.8), (14, "verde", 5.1)],
                    14 : [(14, "verde", 5.1)]}

def a_estrela(origem, destino):
    fronteiras_abertas = []
    fronteiras_abertas.append(origem)
    dic_aux = {}
    
    while(fronteiras_abertas != 0):
        estado_atual = origem
        vizinhos = distancias_reais[estado_atual] #colocando a lista de tuplas para estabelecer vizinhos
        for i in vizinhos:
            fronteiras_abertas.append(i[0]) #colocar os proximos estados na fronteira
            dic_aux[i[0]] = (i[1], i[2])
            
            
a_estrela(2, 8)

        

            

# execute o algoritmo de pesquisa em largura em cada um desses grafos para encontrar a solução

inicio = {
    'A': {
        'F': "Fim"
    },
    'B': {
        'C' : None,
        'D':{
            'F': "Fim"
        }
    }
}


def encontrar_caminho(caminho, objetivo, path=[]):
    for chave, valor in caminho.items():
        caminho = path + [chave]
        if isinstance(valor, dict):
            encontrar_caminho(valor, objetivo, caminho)
        elif valor == objetivo:
            print(caminho)

            
encontrar_caminho(inicio, "Fim") # --> A, F
# ['A', 'F']
# ['B', 'D', 'F']
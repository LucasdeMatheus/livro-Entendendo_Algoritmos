# Encontre o menor caminho de "jato" até "gato"
# -- acredito que seja 'gado', não 'gato', já que no livro diz que "fim" se localiza no gado, e o gabarito tambem condiz isso.


inicio = {
    "jato":{
        "gato":{
            'gado': "Fim",
            'grato':{
                'gado': 'Fim'
            }
        },
        'tato':{
            "gato":{
                'gado': 'Fim'
            },
            "chato":{
                'gado': 'Fim'
            }
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


encontrar_caminho(inicio, "Fim") # --> 25e
# ['jato', 'gato', 'gado']
# ['jato', 'gato', 'grato', 'gado']
# ['jato', 'tato', 'gato', 'gado']
# ['jato', 'tato', 'chato', 'gado']
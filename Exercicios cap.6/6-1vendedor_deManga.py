from collections import deque

# vendedor
def pessoa_e_vendedor(nome):
    return nome[-1] == "m"

grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["alice"] = ["peggy"]
grafo["bob"] = ["peggy", "anuj"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []


def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo["voce"]
    
    verificadas = []
    
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        
        if not pessoa in verificadas: # se a pessoa não estiver na lista verificadas
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " é um vendedor de manga!")
                break
                # return True

            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa) # adiciona pessoa na lista de verificadas
    # return False

    # caso o while quebre sozinho
    else:
        print("Não há vendedores de manga nesta rede.") 

    print(verificadas)



pesquisa(grafo)
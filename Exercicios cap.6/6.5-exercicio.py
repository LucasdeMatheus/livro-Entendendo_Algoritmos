# Quais desses grafos também são árvores?

# Grafo A
#       x
#     / \
#    x   x
#  / \
# x   x

# representado em código
grafoA = {}

grafoA["1"] = ["2", "3"]
grafoA['2'] = ["4", "5"]

# --> é uma árvore

# Grafo B
#       x  < -
#     / \    \  
#    x   x    \ 
#   ^\  / \   |  
#     x   x _/
# eles se retornam(ciclo)

# represenado em código

grafoB = {}

grafoB["1"] = ["2", "3"]
grafoB['3'] = ["4", "5"]
grafoB['4'] = ['2']
grafoB['5'] = ['1']

# --> não é uma arvore, pois faz um ciclo, o 4 chama o 2, e o 5 chama o 1


# Grafo C
#       x        
#      / \
#     x   x
#    /
#   x
# ela está deitada no livro.

# represenado em código
grafoC = {}

grafoC["1"] = ["2", "3"]
grafoC["2"] = ["4"]

# --> é uma arvore, a pegadinha era que no livro esta arvore está deitada, mas não faz diferença. 
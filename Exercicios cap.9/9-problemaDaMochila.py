objetos = {
    'violao':{
        'kg': 1,
        'valor': 1500
    },
    'radio': {
        'kg': 4,
        'valor': 3000
    },
    'notebook':{
        'kg': 3,
        'valor': 2000
    }
}
mochila = {
    'kg': 4,
    'valor': None
}
tabela = [[None for _ in range(mochila['kg'])] for _ in objetos]

linha = 0
for objeto in objetos:
    print(objetos[objeto]['kg'])
    coluna = 0
    while coluna < mochila['kg']:
        if objetos[objeto]['kg'] <= coluna + 1:
            tabela[linha][coluna] = objetos[objeto]['valorz']
        coluna += 1
        
    linha += 1

for i in range(len(tabela)):
    for j in range(len(tabela[i])):
        if tabela[i][j] is None:
            tabela[i][j] = tabela[i-1][j]
            

print(tabela)
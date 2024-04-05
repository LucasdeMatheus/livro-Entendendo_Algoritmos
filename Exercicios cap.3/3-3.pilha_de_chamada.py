def sauda(nome):
    print (f'Olá, {nome}!') # 2- print
    sauda2(nome) # 3- função 2 é chamada
    print(f'preparando para dizer tchau...') # 5- print
    tchau() # 6- função tchau() é chamada
    # fim da função, encerra pilha de chamada
    
def sauda2(nome):
    print(f'como vai {nome}?') # 4- print
    # fim da função, retorna de onde parou

def tchau():
    print('ok, tchau!') # 7- print
    # fim da função, retorna de onde parou

sauda('Lucas') # 1- função é chamada
def procure_pela_chave2(caixa_principal):
    pilha = [caixa_principal] 
    while pilha:  
        caixa_atual = pilha.pop() 
        for item in caixa_atual: 
            if isinstance(item, list):  
                pilha.append(item)  
            elif item == "Chave":  
                print('Achei a chave')  


# uso
procure_pela_chave2(caixa_principal)



#mesmo uso, mas simples
def procure_pela_chave(caixa):
    for item in caixa:
        if item == "Chave":
            print("achei a chave")
            return
        elif isinstance(item, list): 
            procure_pela_chave(item)


# Exemplo de uso
caixa_principal = [["Item 1", "Item 2"], ["Item 3", ["Item 4", "Chave"]], "Item 5"]

procure_pela_chave(caixa_principal)


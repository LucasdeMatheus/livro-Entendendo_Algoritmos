# Você tem um nome e deseja encontrar o número de telefone para esse nome em uma agenda telefônica.


# ------------------------------------------- lista telefônica --------------------------------------------

# gerada pelo chatGPT
lista_telefônica = {
    "Alice": "123456789",
    "Bob": "987654321",
    "Carol": "111222333",
    "David": "444555666",
    "Eva": "777888999",
    "Fernando": "111223344",
    "Gabriel": "555666777",
    "Helen": "888999000",
    "Igor": "123443211",
    "Julia": "987654321",
    "Karine": "111222333",
    "Lucas": "444555666",
    "Mariana": "777888999",
    "Nathan": "111223344",
    "Olivia": "555666777",
    "Pedro": "888999000",
    "Quiteria": "123443211",
    "Rafael": "987654321",
    "Sofia": "111222333",
    "Thiago": "444555666",
    "Ursula": "777888999",
    "Victor": "111223344",
    "Wagner": "555666777",
    "Xavier": "888999000",
    "Yasmin": "123443211",
    "Zoe": "987654321"
}

# ------------------------ pesquisa binária ------------------------

def pesquisa_binaria(agenda, nome):
    esquerda = 0
    direita = len(agenda) - 1
    chaves = list(lista_telefônica.keys())
    contador_operações = 0

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        chute = chaves[meio]

        if chute == nome:
            print("Olá")
            print(agenda[nome])
            print(contador_operações)

        if chute > nome:
            direita = meio - 1
        else:
            esquerda = meio + 1
        contador_operações += 1
        
    return None
    
    

pesquisa_binaria(lista_telefônica, "Bob") # Bob, 987654321, 4 --> Nome, telefone, e o contador de operações
        
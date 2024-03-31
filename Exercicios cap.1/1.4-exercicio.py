# Você tem um número de telefone e deseja encontrar o dono dele em uma agenda telefônica. 
# (Dica: Deve procurar pela agenda inteira!)

# -------------------------------------------------- lista telefônica -----------------------------------------------------

# gerada pelo chatGP
lista_telefônica = {
    "Alice": "123456789",
    "Bob": "987354321",
    "Carol": "111222233",
    "David": "434555666",
    "Eva": "777888199",
    "Fernando": "111223343",
    "Gabriel": "555666737",
    "Helen": "888999100",
    "Igor": "123443231",
    "Julia": "987624321",
    "Karine": "111222333",
    "Lucas": "444555666",
    "Mariana": "772888999",
    "Nathan": "111223344",
    "Olivia": "555666772",
    "Pedro": "888999001",
    "Quiteria": "123443221",
    "Rafael": "987614321",
    "Sofia": "112222333",
    "Thiago": "444355666",
    "Ursula": "777888999",
    "Victor": "111213344",
    "Wagner": "555666777",
    "Xavier": "888999000",
    "Yasmin": "123443212",
    "Zoe": "987654321"
}
 
# ----------------------------- pesquisa simples -------------------------------

def pesquisa_simples(agenda, numero):
    contador_operações = 0
    for chaves in agenda.items():
        if chaves[1] == numero:
            print(chaves[0])



pesquisa_simples(lista_telefônica, "555666777")# Wagner --> chave com este valor 
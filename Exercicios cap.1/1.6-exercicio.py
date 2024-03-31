# Você quer ler os números apenas dos nomes que começam com A.


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
    "Zoe": "987654321",
}



# ----------------------------- pesquisa por inicial ---------------------------


def pesquisa_inicial(agenda, inicial):
    for chaves in agenda.items():
        if chaves[0][0] == inicial:
            print(f"Nome: {chaves[0]}\nNumero: {chaves[1]}")

pesquisa_inicial(lista_telefônica, "B")
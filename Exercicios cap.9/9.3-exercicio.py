# Algoritmo para solucionar erros de ortografia


def longest_common_substring(palavra_a, palavra_b):
    # Tamanhos
    linhas = len(palavra_a) + 1
    colunas = len(palavra_b) + 1

    # Inicializa a tabela com zeros
    tabela = [[0 for _ in range(colunas)] for _ in range(linhas)]

    # Preenche a tabela
    for i in range(1, linhas):
        for j in range(1, colunas):
            if palavra_a[i - 1] == palavra_b[j - 1]:
                tabela[i][j] = tabela[i - 1][j - 1] + 1
            else:
                tabela[i][j] = 0

    # Impressão da tabela com cabeçalhos
    print("    ", end="")
    for letra in palavra_b:
        print(f"{letra} ", end="")
    print()
    
    for i in range(linhas):
        if i == 0:
            print("  ", end="")
        else:
            print(f"{palavra_a[i - 1]} ", end="")
        for j in range(colunas):
            print(f"{tabela[i][j]} ", end="")
        print()

# suponha que você pesquise por HISH, HISH não existe, iremos testar com FISH, em seguida com VISTA
longest_common_substring("FISH", "HISH")
# saída:
#     H I S H
#   0 0 0 0 0
# F 0 0 0 0 0
# I 0 0 1 0 0 --> se as letras forem iguais, o valor será x + 1
# S 0 0 0 2 0
# H 0 1 0 0 3

# x = valor do indice superior e anterior esquerdo.

longest_common_substring("FISH", "VISTA")
# saída:
#     V I S T A 
#   0 0 0 0 0 0 
# F 0 0 0 0 0 0 
# I 0 0 1 0 0 0 
# S 0 0 0 2 0 0 
# H 0 0 0 0 0 0 
#             ^ não é a resposta final, pois nesse algoritmo, o maior numero da tabela é a solução
# a primeira saída é mais viavel, pois termina com um numero maior(3).

# outro caso: FOSH, quis dizer FISH ou FORT?

longest_common_substring("FOSH", "FISH")
# saída:
#     F I S H
#   0 0 0 0 0
# F 0 1 0 0 0
# O 0 0 0 0 0
# S 0 0 0 1 0
# H 0 0 0 0 2

longest_common_substring("FOSH", "FORT")

# saída
#     F O R T
#   0 0 0 0 0
# F 0 1 0 0 0
# O 0 0 2 0 0
# S 0 0 0 0 0
# H 0 0 0 0 0

# observe que, em ambos os testes, os numeros maiores são iguais(2). 
# Porém, fish é mais parecido, pois tem mais letras semelhante

# Para esse caso, a solução é modificar a função para sempre herdar o valor superior esquerdo, ao invés de 0

def longest_common_substring_V2(palavra_a, palavra_b):
    # Tamanhos
    linhas = len(palavra_a) + 1
    colunas = len(palavra_b) + 1

    # Inicializa a tabela com zeros
    tabela = [[0 for _ in range(colunas)] for _ in range(linhas)]

    # Preenche a tabela
    for i in range(1, linhas):
        for j in range(1, colunas):
            if palavra_a[i - 1] == palavra_b[j - 1]:
                tabela[i][j] = tabela[i - 1][j - 1] + 1
            else:
                tabela[i][j] = max(tabela[i - 1][j], tabela[i][j - 1]) # modificado

    # Impressão da tabela com cabeçalhos
    print("    ", end="")
    for letra in palavra_b:
        print(f"{letra} ", end="")
    print()
    
    for i in range(linhas):
        if i == 0:
            print("  ", end="")
        else:
            print(f"{palavra_a[i - 1]} ", end="")
        for j in range(colunas):
            print(f"{tabela[i][j]} ", end="")
        print()


# testando novamente
print("")
longest_common_substring_V2("FOSH", "FISH")
# saída:
#   F I S H
#   0 0 0 0 0
# F 0 1 1 1 1
# O 0 1 1 1 1
# S 0 1 1 2 2
# H 0 1 1 2 3

longest_common_substring_V2("FOSH", "FORT")
# saída:
#  F O R T
#  0 0 0 0 0
# F 0 1 1 1 1
# O 0 1 2 2 2
# S 0 1 2 2 2
# H 0 1 2 2 2

# observe que agora FISH tem o maior numero, e é a resposta mais viavel, como esperado.

# EXERCICIO 9.3 Desenhe e preencha uma tabela para calcular a maior substring comum entre
# blue (azul, em inglês) e clues(pistas, em inglês)

# função ja feita, apenas irei chamar-la
longest_common_substring_V2("BLUE", "CLUES")
# saída:
#     C L U E S
#   0 0 0 0 0 0
# B 0 0 0 0 0 0
# L 0 0 1 1 1 1
# U 0 0 1 2 2 2
# E 0 0 1 2 3 3
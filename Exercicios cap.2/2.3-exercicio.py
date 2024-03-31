# Vamos analisar um experimento.
#  Imagine que o Facebook guarda uma lista de usuários.
#  Quando alguém tenta acessar o Facebook, uma busca é feita pelo nome de usuário.
#  Se o nome da pessoa está na lista, ela pode continuar o acesso.
#  As pessoas acessam o Facebook com muita frequência, então existem muitas buscas nessa lista.
#  Presuma que o facebook usa a pesquisa binária para procurar um nome na lista.
#  A pesquisa binária para procurar um nome na lista.
#  A pesquisa binária requer acesso aleatório -
#  Você precisa ser capaz de acessar o meio da lista de nome instantaneamente.
#  Sabendo disso, você implementaria essa lista como um arrayou uma lista encadeada?


# array


# ------------------------------------------------ lista de nomes ------------------------------------------------

# gerada pelo mano GPT
nomes = {
    'A': ['Ana', 'Arthur', 'Amanda', 'André', 'Alice'],
    'B': ['Bruno', 'Beatriz', 'Bianca', 'Breno', 'Bárbara'],
    'C': ['Carlos', 'Carolina', 'Cristina', 'César', 'Camila'],
    'D': ['Daniel', 'Débora', 'Diego', 'Diana', 'Davi'],
    'E': ['Eduardo', 'Elisa', 'Esther', 'Erick', 'Emily'],
    'F': ['Fernando', 'Fátima', 'Felipe', 'Flávia', 'Fabrício'],
    'G': ['Gabriel', 'Giovanna', 'Gustavo', 'Gisele', 'Guilherme'],
    'H': ['Hugo', 'Helena', 'Henrique', 'Heloísa', 'Heitor'],
    'I': ['Igor', 'Isabela', 'Isaac', 'Ingrid', 'Ivete'],
    'J': ['João', 'Juliana', 'Jorge', 'Jéssica', 'José'],
    'K': ['Kauã', 'Kátia', 'Kleber', 'Karen', 'Kaique'],
    'L': ['Luís', 'Larissa', 'Leonardo', 'Lívia', 'Lucas'],
    'M': ['Maria', 'Marcos', 'Mariana', 'Matheus', 'Monica'],
    'N': ['Natália', 'Nelson', 'Nathalia', 'Nicolas', 'Nina'],
    'O': ['Otávio', 'Olívia', 'Orlando', 'Oliver', 'Otto'],
    'P': ['Pedro', 'Patrícia', 'Paulo', 'Paloma', 'Priscila'],
    'Q': ['Quiteria', 'Quintino', 'Queren', 'Quiterio', 'Quintilio'],
    'R': ['Rafael', 'Renata', 'Roberto', 'Rosa', 'Ricardo'],
    'S': ['Sandra', 'Samuel', 'Sabrina', 'Sérgio', 'Silvia'],
    'T': ['Thiago', 'Tatiane', 'Tiago', 'Tainá', 'Túlio'],
    'U': ['Ubirajara', 'Ubiratã', 'Ulisses', 'Ursula', 'Uira'],
    'V': ['Victor', 'Vanessa', 'Valentina', 'Vinícius', 'Vitória'],
    'W': ['William', 'Wagner', 'Wanessa', 'Wesley', 'Wendy'],
    'X': ['Xavier', 'Ximena', 'Xanddy', 'Xênia', 'Xisto'],
    'Y': ['Yuri', 'Yasmin', 'Yago', 'Yasmin', 'Yara'],
    'Z': ['Zé', 'Zilda', 'Zacarias', 'Zuleica', 'Zoé']
}
# 2.5-exercicio - Obs: essa lista gerada acima, é uma híbrida

# pesquisa binária
def pesquisa_binaria(lista, nome):
    baixo = 0
    alto = len(lista) - 1
    chaves = list(lista.keys())
    inicial = nome[0]
    contador_operações = 0
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = chaves[meio]
        if chute == inicial:
            print(inicial, nome, contador_operações)
            return chute
        elif chute > nome:
            alto = meio - 1
        else:
            baixo = meio + 1
        contador_operações += 1
    return None

pesquisa_binaria(nomes, "Anay78frfrf")
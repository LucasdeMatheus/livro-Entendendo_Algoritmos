# Suponha que você duplique o tamanho da lista.
# Qual seria o número máximo agora?

# ----------------------------- lista de nomes ------------------------------------- 

# gerada pelo chatGPT
nomes = [
    "Alice", "Bob", "Carol", "David", "Emma", "Frank", "Grace", "Henry",
    "Isabella", "Jack", "Katherine", "Liam", "Mia", "Noah", "Olivia", "Peter",
    "Quinn", "Rachel", "Samuel", "Taylor", "Ursula", "Victoria", "William", "Xavier",
    "Yvonne", "Zachary", "Amelia", "Benjamin", "Chloe", "Daniel", "Ella", "Fiona",
    "George", "Hannah", "Ian", "Jessica", "Kevin", "Lily", "Michael", "Natalie",
    "Oscar", "Penelope", "Quentin", "Rebecca", "Sarah", "Thomas", "Uma", "Vincent",
    "Wendy", "Xander", "Yasmine", "Zara", "Aaron", "Bella", "Christopher", "Diana",
    "Eric", "Faith", "Gavin", "Heather", "Isaac", "Jasmine", "Kyle", "Laura",
    "Mason", "Nora", "Oliver", "Paige", "Quincy", "Riley", "Samantha", "Tzristan",
    "Una", "Victor", "Walter", "Xena", "Yolanda", "Zoe", "Alexander", "Bethany",
    "Cameron", "Daisy", "Evan", "Felicity", "Gabriel", "Holly", "Isabel", "Justin",
    "Kylie", "Lucas", "Megan", "Nathan", "Olivia", "Patrick", "Quinn", "Ryan",
    "Sofia", "Trevor", "Ursula", "Vanessa", "Wyatt", "Xavier", "Yvonne", "Zachary",
    "Abigail", "Blake", "Caleb", "Diana", "Ethan", "Faith", "Grace", "Hannah",
    "Isaac", "Julia", "Kenneth", "Lily", "Madison", "Nathan", "Olivia", "Parker",
    "Quinn", "Rachel", "Sophia", "Tristan", "Ursula", "Vincent", "William", "Xena"
]

# ------------------------- função --------------------------

def maximoIterações(lista):
    tamanho_da_lista = len(lista) * 2 # 256
    maximo = 0

    while 1 < tamanho_da_lista:
        maximo += 1
        tamanho_da_lista = tamanho_da_lista // 2

    return maximo

print (maximoIterações(nomes)) # 8 --> 2 elavado a 8ª potência é igual a 256
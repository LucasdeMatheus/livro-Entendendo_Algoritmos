# suponha que você esteja criando um aplicativo para acompanhar as suas finanças
# todos os dias vocÊ anotará o que gastou e onde gastou.
# No final do mês, você deverá revisar os seus gastos e resumir p quanto gastou.
# Logo, você terá um monte de inserções e poucas leituras. Você deverá usar array ou uma lista para implementear este

# lista encadeada



# ----------------------------------------- funções ----------------------------------------------------

# classe de um nó na lista encadeada, o que vai atribuir os valores
class No:

    # função para atribuir as compras quando for chamado quando um novo objeto No é criado
    def __init__(self, dia, compra, valor):
        self.dia = dia
        self.compra = compra
        self.valor = valor
        self.proximo = None

# Clase Registrar_compras, essa classe irá gerenciar os registros de compras
class Registrar_compras:

    # esta função irá criar uma nova lista vazia
    def __init__(self):
        self.cabeca = None

    # função para adicionar uma compra
    def adicionar_gasto(self, dia, compra, valor):

        # criando novo objeto com os parâmetros em questão
        novo_no = No(dia, compra, valor)

        # "se a lista estiver vazia, self.cabeca será novo_no"
        if self.cabeca is None:
            self.cabeca = novo_no

        # "se não, adicionar continuamente"
        else:
            # aqui irão correr pela lista toda, até chegar no final da lista
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    # função calcular todos os gastos
    def calcular_mês(self):
        total = 0
        atual = self.cabeca
        while atual:
            total += atual.valor
            atual = atual.proximo
        print(f"Total gasto: R${total},00")

    # função para impressão dos registros
    def imprimir_registros(self):
        print("Compra -------- Valor ------ Dia\n")
        atual = self.cabeca
        while atual:
            print(f"{atual.compra} ------ R${atual.valor},00 ------ {atual.dia}")
            atual = atual.proximo

# Criar instância da classe Registrar_compras
registro = Registrar_compras()

# Registrando compras manualmente
registro.adicionar_gasto("2024-03-01", "cinema -", 32)
registro.adicionar_gasto("2024-03-01", "fast-food", 50)
registro.adicionar_gasto("2024-03-05", "fast-food", 92)
registro.adicionar_gasto("2024-03-21", "cinema -", 32)
registro.adicionar_gasto("2024-03-25", "netflix ", 45)

# Imprimir todas as compras
registro.imprimir_registros()

# Imprimir valor total de gastos
registro.calcular_mês()

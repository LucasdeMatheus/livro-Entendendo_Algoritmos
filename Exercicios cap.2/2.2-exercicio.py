# Suponha que você esteja criando um aplicativo para anotar os pedidos dos clientes em um restaurante.
#  Seu aplicativo precisa de uma lista de pedidos.
#  Os garçons adicionam os pedidos a essa lista e os chefes retiram os pedidos da lista.
#  Funciona como uma fila.
#  Os garçons colocam os pedidos no final da fila e os chefes retiram os pedidos do começo dela para cozinha-los

# lista encadeada 


# ------------------------------------------------------ funções ------------------------------------------------------


# class No
class No:
    def __init__(self, pedido, mesa):
        self.mesa = mesa
        self.pedido = pedido
        self.proximo = None

# Gerenciador dos pedidos
class Novo_pedido:

    # primeiro objeto
    def __init__(self):
        self.cabeca = None

    # adicionar novo pedido
    def adicionar_pedido(self, pedido, mesa):
        novo_no = No(pedido, mesa)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    # imprimir registros de pedidos
    def imprimir_pedidos(self):
        print("nº -------- pedido ------ mesa\n")
        atual = self.cabeca
        numero_pedido = 1
        while atual:
            print(f"{numero_pedido} ------ {atual.pedido} ------ {atual.mesa}")
            atual = atual.proximo
            numero_pedido +=1


# instância
pedido = Novo_pedido()

# pedidos
pedido.adicionar_pedido("lagosta", 3)
pedido.adicionar_pedido("suco", 5)
pedido.adicionar_pedido("hamburguer", 2)
pedido.adicionar_pedido("pizza", 3)
pedido.adicionar_pedido("agua", 1)
pedido.adicionar_pedido("feijoada", 4)
pedido.adicionar_pedido("espaguete", 2)


pedido.imprimir_pedidos()
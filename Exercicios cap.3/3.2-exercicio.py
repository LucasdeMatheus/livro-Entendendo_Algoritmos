#  Suponha que você acidentalmente escreva uma função recursiva que fique executando infinitamente.
#  Como você viu, seu computador aloca memória na pilha cada chamada de função.
#  O que acontece com a pilha quando a função recursiva fica execuntando infinitamente.



def callInfinit():
    print('infinito')
    callInfinit()

callInfinit()

# ---> RecursionError: maximum recursion depth exceeded

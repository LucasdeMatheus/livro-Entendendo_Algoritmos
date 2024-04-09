#  criar uma tabela de multiplicação com todos os elementos do array.
#  Assim, caso o seu array seja [2, 3, 7, 8, 10], você primeiro multiplicará cada elemento por 2.
#  Depois, multiplicará cada elemento por 3 e então por 7, e assim por diante.


def multiplicar(array):
    if len(array) == 2:
        return array[0]*array[1]
    else:
        
        return array[0] * multiplicar(array[1:])

print(multiplicar([1,2,3]))

# --> O(n²)
# Escreva o código para a função soma, vista anteriormente



def soma(arr):
    if arr == []:
        return 0
    return arr[0] + soma(arr[1:])

print(soma([1,2,3]))
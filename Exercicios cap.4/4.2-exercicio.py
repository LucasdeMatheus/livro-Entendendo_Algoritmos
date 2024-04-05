# Escreva uma função recursiva que conte o n´mero de itens em uma lista

def counter(arr):
    if arr == []: 
        return True
    return 1 + counter(arr[1:])


print(counter([1,2,3,4,5]))
# Duplica o valor de cada elemento em um array

def duplicar(array):
    arr = []
    for i in range(len(array)):
        arr.append(array[i])
        arr.append(array[i])

    return arr

print(duplicar([2,5,6]))

# --> O(n)
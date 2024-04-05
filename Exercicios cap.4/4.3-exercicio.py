
def max(arr):
    if len(arr) == []:
        return sub_max
    elif len(arr) == 1: # se tiver um indice, ele será o maior
        return arr[0]
    else:
        sub_max = max(arr[1:]) # será o indice 1 da array na recursão
        if arr[0] > sub_max: 
            return arr[0]
        else:
            return sub_max


print(max([5,0,12,9,1,2]))
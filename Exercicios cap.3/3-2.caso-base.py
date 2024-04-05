'''
# loop infinito

def regressiva(i):
    print(i)
    regressiva(i-1)

regressiva(5) # ----> recursão excede o limite, mas continua sendo um loop
# RecursionError: maximum recursion depth exceeded


# Ctrl + C interrompe o script
'''

def regressiva(i):
    print(i)
    if i <= 1: # caso-base
        return
    else:      # caso recursivo
        regressiva(i-1)

regressiva(5) # ---> 5 4 3 2 1
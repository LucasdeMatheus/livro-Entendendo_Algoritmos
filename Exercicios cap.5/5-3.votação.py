votaram = {}

valor = votaram.get("tom")

def vereficar_eleitor(nome):
    if votaram.get(nome):
        print("Mande embora!")
    else:
        votaram[nome] = True
        print("Deixe votar!")

vereficar_eleitor("tom")
# Deixe votar!

vereficar_eleitor("mike")
# Deixe votar!

vereficar_eleitor("mike")
# Mande embora!
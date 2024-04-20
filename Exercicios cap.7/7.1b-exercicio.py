grafo = {
    "inicio": {"A": 10},
    "A": {"B": 20},
    "B": {"C": 1, "fim": 30},
    "C": {"A": 1},
}

infinito = float("inf")
custos = {nodo: infinito for nodo in grafo}
custos["inicio"] = 0
custos["fim"] = infinito

def ache_no_custo_mais_baixo(custos, processados):
    custo_mais_baixo = float("inf")
    nodo_mais_baixo = None
    for nodo, custo in custos.items():
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_mais_baixo = nodo
    return nodo_mais_baixo

processados = []

nodo = ache_no_custo_mais_baixo(custos, processados)

while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo.get(nodo, {})  # Usando grafo.get() para lidar com chaves ausentes
    for n, custo_vizinho in vizinhos.items():
        novo_custo = custo + custo_vizinho
        if custos.get(n, infinito) > novo_custo:  # Usando custos.get() para lidar com chaves ausentes
            custos[n] = novo_custo
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos, processados)

print("Custos mínimos:", custos["fim"]) # fim: 60
# inicio --> A: 10 --> B: 20 -- fim: 30 == 60


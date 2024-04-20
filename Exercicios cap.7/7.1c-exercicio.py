grafo = {
    "inicio": {"A": 2, "B": 2},
    "A": {"fim": 2, "C": 2},
    "B": {"A": 2},
    "C": {"fim": 2, "B": 2},
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

print("Custos mínimos:", custos["fim"]) # fim: 4
# inicio --> A: 2 --> fim: 2 == 4


def ache_no_custo_mais_baixo(custos, processados):
    custo_mais_baixo = float("inf")
    nodo_mais_baixo = None
    for nodo, custo in custos.items():
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_mais_baixo = nodo
    return nodo_mais_baixo

grafo = {
    "inicio": {"A": 6, "B": 2},
    "A": {"fim": 1},
    "B": {"A": 3, "fim": 5},
    "fim": {}
}

infinito = float("inf")

custos = {nodo: infinito for nodo in grafo}
custos["inicio"] = 0

pais = {nodo: None for nodo in grafo}

processados = []

nodo = ache_no_custo_mais_baixo(custos, processados)

while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo.get(nodo, {})
    for n, custo_vizinho in vizinhos.items():
        novo_custo = custo + custo_vizinho
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos, processados)

print("Custos mínimos:", custos)
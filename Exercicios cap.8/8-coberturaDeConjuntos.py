#                   ^
# >> arr = [1, 2, 2, 3, 3, 3]
# >> set(arr)
# set([1, 2, 3])
#         ^
#     conjunto


estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "dq", "as"])

estacoes = {}
estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "id", "mt"])
estacoes["ktres"] = set(["or", "nv", "ca"])
estacoes["kquatro"] = set(["nv", "ut"])
estacoes["kcinco"] = set(["ca", "az"])

estacoes_final = set()
while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()
    for estacao, estados in estacoes.items():
        cobertos = estados_abranger & estados
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos
    estados_abranger -= estados_cobertos
    estacoes_finais.add(melhor_estacao)
    
print(estacoes_finais)

# essa porra n funciona kkkkkkkk


# 1-
# frutas = set(["abacate", "tomate", "banana"])
# vegetais = set(["beterraba", "cenoura", "tomate"])

# "&" interseção: pega o que tem em comum
# >> fruits & Vegatais
# >> tomate

# "|" união: junta os dois
# >> fruits | Vegatais
# >> (["abacate", "tomate", "banana", "beterraba", "cenoura", "tomate"])

# "-" diferença: subtrai entre
# >> fruits - Vegatais
# >> "abacate", "banana"

# >> fruits - Vegatais
# >> "beterraba", "cenoura"


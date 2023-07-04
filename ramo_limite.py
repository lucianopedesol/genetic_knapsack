

class Item:
    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso

def ramo_e_limite_mochila(capacidade_maxima, itens):
    n = len(itens)
    melhor_valor = 0
    melhor_solucao = []

    def calcular_limite_inferior(indice, valor_atual, peso_atual):
        limite = valor_atual
        peso_restante = capacidade_maxima - peso_atual
        i = indice + 1

        while i < n and peso_restante > 0:
            if itens[i].peso <= peso_restante:
                limite += itens[i].valor
                peso_restante -= itens[i].peso
            else:
                limite += (peso_restante / itens[i].peso) * itens[i].valor
                break

            i += 1

        return limite

    def ramo_e_limite_recursivo(indice, valor_atual, peso_atual, solucao_atual):
        nonlocal melhor_valor, melhor_solucao

        if indice >= n or peso_atual >= capacidade_maxima:
            return

        limite_inferior = calcular_limite_inferior(indice, valor_atual, peso_atual)

        if limite_inferior < melhor_valor:
            return

        if valor_atual > melhor_valor:
            melhor_valor = valor_atual
            melhor_solucao = solucao_atual[:]

        item_atual = itens[indice]

        # Incluir o item atual na mochila
        if peso_atual + item_atual.peso <= capacidade_maxima:
            solucao_atual.append(indice)
            ramo_e_limite_recursivo(indice + 1, valor_atual + item_atual.valor,
                                    peso_atual + item_atual.peso, solucao_atual)
            solucao_atual.pop()

        # Excluir o item atual da mochila
        ramo_e_limite_recursivo(indice + 1, valor_atual, peso_atual, solucao_atual)

    ramo_e_limite_recursivo(0, 0, 0, [])
    return melhor_valor, melhor_solucao

# Exemplo de utilização
itens = [
    Item(10, 5), 
    Item(8, 2), 
    Item(15, 8), 
    Item(12, 3), 
    Item(20, 10), 
]

 

capacidade_maxima = 50

melhor_valor, melhor_solucao = ramo_e_limite_mochila(capacidade_maxima, itens)

print("Melhor valor encontrado:", melhor_valor)
print("Melhor solução encontrada (índices dos itens):", melhor_solucao)

 

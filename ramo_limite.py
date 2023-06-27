'''
O algoritmo genético é uma abordagem heurística baseada em evolução que tenta encontrar soluções 
ótimas através de operadores genéticos, como seleção, cruzamento e mutação. Ele é adequado 
para problemas de otimização combinatória, como o problema da mochila, onde é necessário 
encontrar uma solução de alta qualidade, mas não necessariamente a solução ótima.

O algoritmo do Ramo e Limite é uma abordagem exata que busca explorar todo o espaço de 
solução de forma sistemática. Ele divide o problema em subproblemas menores e utiliza limites 
inferiores para eliminar soluções inviáveis ou subótimas. Essa abordagem garante a obtenção 
da solução ótima, mas pode ser computacionalmente intensiva, especialmente para problemas grandes.

Portanto, a escolha entre os algoritmos depende das características específicas do problema e das 
necessidades do contexto. O algoritmo genético pode ser mais rápido e eficiente em problemas de grande 
escala, enquanto o algoritmo do Ramo e Limite é mais adequado quando se deseja garantir a solução ótima.

É importante ressaltar que cada algoritmo possui vantagens e limitações. O algoritmo genético é 
uma heurística que depende de parâmetros de configuração e pode não encontrar a solução ótima 
em todos os casos. Já o algoritmo do Ramo e Limite é exato, mas pode se tornar impraticável 
para problemas muito grandes devido à complexidade computacional.

'''

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

 
def knapsack(items, capacity):
    # Inicializando uma matriz para armazenar os valores máximos possíveis para diferentes capacidades e número de itens
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Preenchendo a matriz dp usando a abordagem de programação dinâmica
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            weight = items[i - 1][0]
            value = items[i - 1][1]
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    # Reconstruindo a solução a partir da matriz dp
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][0]

    return dp[n][capacity], selected_items

# Exemplo de uso
items = [
    (15, 15, 'Saco de dormir'),
    (3, 7, 'Corda'),
    (2, 10, 'Canivete'),
    (5, 5, 'Tocha'),
    (9, 8, 'Garrafa'),
    (20, 17, 'Comida'),
]
capacity = 30
max_value, selected_items = knapsack(items, capacity)
print("Valor máximo que pode ser carregado:", max_value)
print("Itens selecionados:")
for item in selected_items:
    print("Item:", item[:-1], "Peso:", item[0], "Pontos:", item[1])

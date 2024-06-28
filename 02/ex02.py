def obter_lucro_maximo(precos: list[float]) -> float:
    preco_minimo = float("inf")
    lucro_maximo = 0

    for preco in precos:
        if preco < preco_minimo:
            preco_minimo = preco

        lucro = preco - preco_minimo

        if lucro > lucro_maximo:
            lucro_maximo = lucro

    return lucro_maximo

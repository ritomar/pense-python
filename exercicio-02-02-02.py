"""
    Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%.
    O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional.
    Qual é o custo total de atacado para 60 cópias?
    R. 945.45
"""

QUANTIDADE = 60
TRANSPORTE = 3.00 + ((QUANTIDADE - 1) * 0.75)

preco_capa = 24.95
preco_livraria = preco_capa * 0.60

total_atacado = (preco_livraria * QUANTIDADE) + TRANSPORTE
print(f'{total_atacado:.2f}')

#Peça o valor de um produto e mostre o valor com 10% de desconto.

print("-- CÁLCULO DE DESCONTO --")
produto = float(input("Informe o valor do produto: R$ "))

desconto = produto * 0.10
produtoDesconto = (produto-desconto)

print("Você terá um desconto de 10%! Total com o desconto aplicado: R$", produtoDesconto)

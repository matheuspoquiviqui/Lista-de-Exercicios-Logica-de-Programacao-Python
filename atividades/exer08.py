'''
Peça a idade do usuário e informe:
"Maior de idade" (18 ou mais)
"Menor de idade"

'''

print("-- MAIOR DE IDADE --")
idade = int(input("Escreva sua idade:"))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
''' 
Peça um número ao usuário. Mostre:
"Número positivo" se for maior que 0
"Número negativo" se for menor que 0
"Zero" se for igual a 0

'''

print("-- TIPOS DE NÚMEROS --")
num = float(input("Escreva um número:"))

if num > 0:
    print("O número é positivo!")
elif num < 0:
    print("O número é negativo!")
else:
    print ("O número é Zero!")
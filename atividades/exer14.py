#Peça 5 números e mostre qual foi o maior número digitado.

print("-- MAIOR NÚMERO --")
maior = 0

for i in range(5):
    numero = int(input("Informe um número: "))
    if numero > maior :
        maior = numero
    
print("O maior número é: ", maior)
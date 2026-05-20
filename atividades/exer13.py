#Peça um número ao usuário 5 números e mostre a soma deles

print("-- SOMA DE 5 NÚMEROS --")
soma = 0

for i in range(5):
    #numero = int(input(f"Informe o {i}° número:")) Desta forma você consegue informar a volta do loop
    numero = int(input("Informe um número para soma: "))
    soma = soma + numero
    
print("A soma dos cinco números é: ", soma)
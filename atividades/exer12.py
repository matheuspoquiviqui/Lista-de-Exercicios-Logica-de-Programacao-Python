# Peça um número ao usuário e mostre a tabuada dele.

print("-- TABUADA --")
numero = int(input("Informe um número inteiro: "))

for i in range (1,11):
    resultado = numero * i
    print (numero, "x", i, "=", resultado)
    
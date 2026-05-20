'''
Peça a nota de um aluno. Mostre:
Aprovado se nota ≥ 7
Recuperação se nota entre 5 e 6.9
Reprovado se menor que 5

'''

print("-- CLASSIFICAÇÃO DE NOTA --")
nota = float(input("Escreva a nota de um aluno:"))

if nota >= 7:
    print("Aluno está Aprovado!")
elif nota >= 5 and nota <= 6.9:
    print("Aluno está em Recuperação!")
else:
    print("Aluno está Reprovado!")
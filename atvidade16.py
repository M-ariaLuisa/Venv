import os
os.system("cls")


print("Laço de repetição - While")

while True:
    nota = float(input("Informe a nota do aluno(a):"))
    if 0 <= nota <= 10:
        break
print(f"nota:{nota}")
print("Fim")
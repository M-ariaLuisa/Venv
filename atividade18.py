import os
os.system("cls")

import os
os.system("cls")


print("Laço de repetição - While")

while True:
    nota_1 = float(input("Informe a 1ª nota do aluno(a):"))
    nota_2 = float(input("Informe a 2ª nota do aluno(a):"))

    if 0 <= nota_1 <= 10 and 0 < nota_2 <= 10:
        break

media = (nota_1 + nota_2) / 2
print(f"Média: {media}")

print("Fim")
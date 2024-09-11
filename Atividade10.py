# Crie um programa que receba um número inteiro e informe se ele é par ou ímpar.
n = float(input("Número: "))
r = n%2
if r == 0:
    print (f"O número {n} é par.")

else:
    print (f"O número {n} é ímpar.")

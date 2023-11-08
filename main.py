# Exercicio 15
soma = 0

for numero in range(0, 100+1):
  soma += numero
  
print(f"A soma dos números de 0 a 100 é: {soma} - {numero}")


print("----------------------------------------")
# Exercicio 16


numero = int(input("Digite um número: "))

for i in range(0, numero+1):
  print(i)


print("----------------------------------------")
# Exercicio 17


for numero in range(0, 11, 2):
  if numero % 2 == 0:
    print(numero)


print("----------------------------------------")
# Exercicio 18


for numero in range(1, 11, 2):
  #if numero % 2 != 0:
    print(numero)

# fim
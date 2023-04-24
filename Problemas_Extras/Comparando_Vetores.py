# Comparando Vetores
# O programa deve imprimir:
    # Os números cujas posições nos vetores coincidem e em que posição se encontram
    # Os demais números, que estão na mesma posição mas cujos valores não coincidem, com o valor de cada vetor e a posição
# Deve usar listas
lista1 = list(range(1,6))
lista2 = list(range(1,6))

# Entrada de dados:
for n in range(0, 5):
    print("Informe o número da posição ", n+1, " da primeira lista")
    lista1[n] = int(input())

for n in range(0, 5):
    print("Informe o número da posição ", n+1, " da segunda lista lista")
    lista2[n] = int(input())


for n in range(0, 5):
    if lista1[n] == lista2[n]:
        print("Coincidência do valor ", lista1[n], " na posição ", n+1)
    else:
        print("Valores ", lista1[n], " e ", lista2[n], " diferentes na posição ", n+1) 
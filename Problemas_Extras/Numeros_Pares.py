# Números Pares
# Escreva um programa em que usuário informa 5 números inteiros
# O programa deve garantir que os valores informados são maiores que zero
# O programa faz a leitura dos números
# O programa imprime apenas os números pares, informando sua posição
# Deve usar listas
lista = list(range(0,5))

invalido = False

for n in range(0, 5):
    print("Informe o número da posição ", n+1)
    lista[n] = int(input())
    while invalido==True:
        if lista[n] <=0:
            print("Valor inválido, tente novamente!")
            lista[n] = int(input())
        else:
            invalido = False


for n in range(0, 5):
    if lista[n] % 2 == 0:
        print("Número na posição ", n+1, " é igual a ", lista[n], " e é par.")
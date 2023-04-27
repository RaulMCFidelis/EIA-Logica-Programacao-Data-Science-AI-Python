# Impressão de Números
# Escreva un programa em que o usuário informe a quantidade de números que irá entrar
# O Programa deve garantir que a quantidade seja igual ou maior que dois
# O programa deve imprimir
    # A soma do primeiro e do último número
    # O produto do primeiro e segundo número informado
# Deve usar listas
quantidade = int( input("Informe a quantidade de números: "))

while quantidade <2:
        print("Quantidade inválida, tente novamente")
        quantidade= int(input())


lista = list(range(0,quantidade))

for n in range(0, quantidade):
    print("Informe o número da posição ", n+1)
    lista[n] = int(input())
 
print(lista)

soma  = lista[0] +  lista[ len(lista)-1] 
print("Soma do primeiro e do último número", lista[0] +  lista[ len(lista)-1])
print("Produto do primeiro e segundo número",  lista[0]  *  lista[1])
# Números Pares
# O programa deve solicitar a entrada de 5 valores inteiros
# O programa deve imp´rimir
    # A quantidade dos valores pares
    # A soma dos valores pares
    # O produto dos valores pares
conta = 0
soma =0
produto = 1

for tab in range(0, 5):
    print("Informe o " + str(tab+1) + "º número: " )
    numero = int(input())
    if numero %  2 == 0:
        conta = conta + 1
        soma = soma + numero
        produto = produto * numero

print("Quantidade de valores pares: ", conta)
print("Soma de valores pares: ", soma)
print("Produto de valores pares: ", produto)

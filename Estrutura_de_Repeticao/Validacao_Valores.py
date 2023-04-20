# Validação de Valores
# O programa deve solicitar a entrada de dois valores inteiros
# Deve garantir que o primeiro valor é maior que 10, e o segundo valor é pelo menos 10 vezes maior que o primeiro valor
# O programa deve imprimir o produto do primeiro valor pelo segundo valor
valido = False
while valido==False:
    val1 = int(input("Informe o primeiro valor: "))
    val2 = int(input("Informe o segundo valor: "))
    if val1>10 and val2>10*val1:
        valido = True
    else:
        print("Valores inválidos!")

print("Produto: ", val1 * val2)
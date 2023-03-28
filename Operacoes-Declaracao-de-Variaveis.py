# Cotação de Moeda
# O usuário deve entrar o valor de moeda estrangeira que quer comprar
# O sistema terá internamente uma variável com a cotação do dia
# O sistema imprime o valor a ser pago em moeda local
# Obs: Deve aceitar valores reais (float)
COTACAO = 3.45
VALOR = input("Informe o valor da moeda estrangeira para compra: ")
VALOR = float(VALOR)
CONVERSAO = VALOR * COTACAO
print("O valor total em moeda local é: ", CONVERSAO)


# Calculadora de Somar Inteiros
# O sistema pede a entrada do primeiro valor, do tipo inteiro
# O sistema pede a entrada do segundo valor, do tipo inteiro
# O sistema imprime a soma dos dois valores
VAL1 = input("Informe o primeiro valor: ")
VAL2 = input("Informe o segundo valor: ")
VAL1 = int(VAL1)
VAL2 = int(VAL2)
VAL3 = VAL1 + VAL2
print("Total dos valores: ", VAL3)

# Versão dois:
VALN = input("Informe o primeiro valor: ")
VALM = input("Informe o segundo valor: ")
print = ("Total dos valores: ", int(VALN) + int(VALM))



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




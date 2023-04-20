# Soma
# Criar um programa que faça a leitura de 5 números inteiros
# O programa deve imprimir a soma dos números
soma = 0
for tab in range(0, 5):
    texto = "Informe o " + str(tab+1) + "º número: " 
    soma = soma + int(input(texto))
print("A soma é igual a : ", soma )
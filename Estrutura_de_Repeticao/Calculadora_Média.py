# Calculadora de Média
# O Programa deve calcular a média dos números informados pelo usuário
# Primeiro o programa deve perguntar, quantos números o usuário vai entrar
# Em seguida ele pede para o usuário entrar cada um dos números
# Por fim, o programa imprime a média dos números
tab = int(input("Quantos números serão calculados? "))
soma = 0
for tab in range(1, tab+1):
    texto = "Informe o " + str(tab) + "º número: " 
    soma = soma + int(input(texto))
print("A média é igual a : ", soma / tab)
# Conversor de Temperatura
# O program deve converter graus para célsios fahrenheit e vice versa através de uma função
# Os números e o tipo de conversão devem ser informados como parâmetros da função
# A função deve retornar o resultado
# O programa deve chamaar a funçãoe imprimir o resultado
def converte(tipo,temp):
    if tipo==1:
        temp = (temp * 9/5) + 32
    else:
        temp = ((temp - 32)* 5) /9
    return temp

tp = int(input("Informe o tipo de conversão 1 para Celsius para Fahrenheit e 2 para Fahrenheit para Celsius : "))
temperatura = int(input("Informe a temperatura para converter: "))

print("O resultado é: ", converte(tp,temperatura ))
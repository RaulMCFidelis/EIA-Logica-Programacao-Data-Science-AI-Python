# Calculadora de Méida
# O programa deve calcular a média de dois números informados pelo usuário
# Os números devem ser informados como parâmetros da função
# A função deve retornar o cálculo
# O programa deve chamar a função e umprimir o resultado
def media(a,b):
    return (a + b) / 2

val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))
resultado = media(val1,val2)
print("O resultado é: ", resultado)
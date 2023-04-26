# Módulo
# O programa deve solicitar a entrada de dois números inteiros
# O programa deve garantir que o segundo seja maior que o primeiro
# O programa deve imprimir o intervalo de número em ordem crescente e decrescente
# A função de impressão deve estar em outro arquivo py, que deve ser importado e executado pelo programa principal
from impressao import imprime
# O arquivo impressao.py deve estar no mesmo diretório
valido = False
while valido == False:
    int1 = int( input("Informe o primeiro valor inteiro: "))
    int2 = int( input("Informe o segundo valor inteiro: "))
    if int2 <= int1:
        print("Valores inválidos! Tente novamente!")
    else:
        valido=True

imprime(int1,int2) 
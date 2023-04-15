# Positivo ou Negativo
# O sistema deve ler um valor inteiro
# Imprimir se o valor for pogitivo e negativo se o valor for negativo e neutro se for zero
val = int(input("Informe um valor: "))
if val<0:
    print("Número Negativo")
elif val>0:
     print("Número Positivo")
else:
    print("Número Neutro")
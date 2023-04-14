# Descontos
# O programa deve ler a quantidade de produtos comprados (int) e o valor (float)
# Deve imprimir:
    # O valor total da compra - sem desconto
    # O valor total da compra - com desconto
    # O Valor da economia
# Qunatidade 2 --> 2% Desconto
# Qunatidade >2 e <=5 --> 5% Desconto
# Qunatidade >5 e <10 --> 10% Desconto
# Qunatidade >= 10 --> 15% Desconto

quantidade = int(input("Informe a quantidade de produtos: "))
total = float(input("Informe valor total da compra: "))
# Desconto = 0% caso seja comprado apenas 1 produto
desconto = 0
if quantidade == 2:
    desconto = 0.02
elif quantidade> 2 and quantidade<=5:
    desconto = 0.05
elif quantidade>5 and quantidade<10:
    desconto = 0.1
elif quantidade >=10:
    desconto = 0.15

#não pode ter else se não vai dar desconto pra 1 produto

calcdesc = total - (total * desconto)

print("Valor Total da Compra: ", total)
print("Valor Total com Desconto: ", calcdesc)
print("Economia: ", total - calcdesc)

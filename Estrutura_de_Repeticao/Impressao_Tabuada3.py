# Tabuada 3
# O programa deve imprimir as rabuadas do 1 ao 10
# Cada tabuada deve ser emoldurada, como no exemplo abaixo:
# ---------------
# | 2 x 1 = 2   |
# | 2 x 2 = 4   |
# | 2 x 3 = 6   |
# | 2 x 4 = 8   |
# | 2 x 5 = 10  |
# | 2 x 6 = 12  |
# | 2 x 7 = 14  |
# | 2 x 8 = 16  |
# | 2 x 9 = 18  |
# | 2 x 10 = 20 |
# ---------------
tab = 1
while tab<11:
    print("--------------------")
    for n in range(1, 11):
        resp =  "|" +  str(n) +  " x " + str(tab) + " = " + str( n * tab )
        esp = "  " * (14 - len(resp)) + "|"
        print(resp + esp)
        if n==10:
            tab = tab + 1
            break
print("--------------------")

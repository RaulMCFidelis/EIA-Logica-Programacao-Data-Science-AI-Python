# Este programa deve ser igual ao anterior, porém, após a impressão, o programa deve perguntar se o usuário quer imprimir uma nova tabuada!
# Se o usuário informar que sim, o usuário deve informar a nova tabuada, que será impressa
# O programa só encerra quando o usuário informar que não quer uma nova impressão
impressao = True
while impressao==True:
    tab = int(input("Informe tabuada que quer imprimir: "))
    for n in range(1, 11):
        print(n, " x ", tab, " = " , n * tab)
    resp = input("Deseja imprimir nova tabuada? Informe S para sim e N para não: ")
    if resp.upper()=="N":
        impressao = False
# Busca de Nomes
# O programa deve ter uma lista com 10 nomes armazenados
# Deve em seguida, pedir ao usuário para entrar um nome
# O programa deve informar se o nome foi ou não encontrado
# O programa não deve fazer distinção entre letra máisculas e minúsculas
lista = ["Raul", "Yasmin", "Twila", "MATHEUS","Fernando", "José", "MARCOS", "ANA", "MARIA", "valentina", "Irene", "Lucas", "Adão", "Eva"]
print("Informe um nome para Localização ")
nome = input()


encontrado = False
for n in range(0, len(lista)):
    print(lista[n])
    if lista[n].lower() == nome.lower():
        encontrado = True

if encontrado==False:
    print("Nome não encontrado")
else:
    print("Nome encontrado")
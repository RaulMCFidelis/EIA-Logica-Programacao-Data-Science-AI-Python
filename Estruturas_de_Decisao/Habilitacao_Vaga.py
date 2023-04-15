# Habilitação para Vaga
# O programa deve perguntar a idade de um candidato a vaga
# O programa ainda deve perguntar a escolaridade, imprimindo as seguintes opções:
    # 1 - Ensino Fundamental
    # 2 - Ensino Médio
    # 3 - Ensino Superior
# O candidato é habilitado a concorrer a vaga se:
    # Tem ensino superior completo ou
    # Tem ensino médio e mais de 60 anos
# Imprimir a mensagem informando se o candidato está habilitado ou não
idade = int(input("Informe a Idade: "))
print("Informe a escolaridade: ")
print("1 – Ensino fundamental")
print("2 – Ensino médio")
print("3 – Ensino superior ")
escolaridade = float(input())

if (escolaridade==3) or (escolaridade==2 and idade>60):
    print("Habilitado!")
else:
    print("Não Habilitado!")

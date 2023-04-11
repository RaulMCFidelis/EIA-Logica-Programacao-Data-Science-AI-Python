# Habilitação para Vaga
    # Para se habilitar a uma vaga de trabalho, o candidato deve cumprir pelo menos um dos requisitos abaixo:
    # Ter meno de 70 anos de idade
    # ter pelo menos 25 anos de atividade profissional
    # Ter mais de 70 e pelo menos 30 anos de atividade profissional
# O programa deve ler estas informações (todas do tipo inteiro) e imprimir se o candidato está ou não habilitado a vaga de trabalho
idade = int(input("Informe a Idade: "))
atividade = float(input("Informe o tempo de atividade profissional: "))
if (idade < 70) or (atividade>=25) or (idade >= 70 and atividade>=30):
    print("Habilitado!")
else:
    print("Não Habilitado")
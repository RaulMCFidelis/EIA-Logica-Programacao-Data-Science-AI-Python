# Alistamento
# O programa deve ler o ano de nascimento de uma pessoa
# O sistema deve imprimir informando se ela está na idade de se alistar ou não (considererando que tiver mais de 18 anos, deve se alistar)
# Considere ler o ano atual do sistema ao invés de usar um ano fixo, usando o exemplo:
# from datetime import date
# year_ = date.today().year
from datetime import date
anonascimento = int(input("Informe o ano de seu nacimento: "))
anoatual = float(date.today().year)
if anoatual-anonascimento > 18:
    print("Deve se alistar!")
else:
    print("Não deve se alistar!")

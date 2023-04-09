# Conceito Final
# O professor deve entrar uma nota no sistema (float)
# O programa deve imprimir o conceito final de acordo com a nota, de acordo com a yabela abaixo:
# >90 - A, >=75 e <=90 - B, >=60 e <75 - C, >=40 e <60 - D, >=20 e <40 - E, <20 - F
nota = float(input("Informe a nota do aluno: "))
if nota>90 :
    print(" Conceito A")
elif nota>=75 and nota <=90 :
    print(" Conceito B")         
elif nota>=60 and nota <75 :
    print(" Conceito C")
elif nota>=40 and nota <60 :
    print(" Conceito D")
elif nota>=20 and nota <40 :
    print(" Conceito E")
else:
    print(" Conceito F") 
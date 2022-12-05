""" Taschenrechner
    erstellt von: Mike
    erstellt am : 22.08.22
    geändert am : 29.08.22
    """
from description import description
description("Taschenrechner")
operator = input('Rechenoperator eingeben(+,-,*,/):')
num_1 = float(input('erste Zahl eingeben'))
num_2 = float(input('zweite Zahl eingeben'))

if operator == "+":
    print('Ergebsnis:', num_1+num_2)
elif operator == "-":
    print('Ergebsnis:',num_1-num_2)
elif operator == "*":
    print('Ergebsnis:',num_1*num_2)
elif operator == "/":
    print('Ergebsnis:',round(num_1/num_2, 2))
else:
    print('falsche Eingabe')


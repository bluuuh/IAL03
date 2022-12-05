import math


num_1 = float(input('erster Widerstand:(nur die Zahl in Ohm)'))
num_2 = float(input('zweiter Widerstand: (nur die Zahl in Ohm)'))

print('Gesamtwiderstand:', round((num_1*num_2)/(num_1+num_2),2),'Ohm')
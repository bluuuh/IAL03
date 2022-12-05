""" Diverse Schleifen
    erstellt von: Mike
    erstellt am : 07.11.22
    geändert am : -

    Das Programm printet Zahlenfolgen die von verschiedenen
    Schleifen generiert werden.
    """
# Zählt von -100 bis 100
i = -100
while i < 101:
    print(i)
    i = i + 10
print("-"*50)

# zählt von 100 runter zu -100 in 10er Schritten
for i in range(100, -101, -10):
    print(i)
print("-"*50)

# zählt von 0 bis 10 und schreibt bei Zahlen größer 5 Hurra! daneben
for i in range(0, 11):
    if i < 5:
        print(i)
    else:
        print(i, "Hurra!")
print("-"*50)

# zählt von 10 runter zu -10 und gibt bei zahlen >=5 gross und <=-5 klein aus
i = 10
while i > -11:
    if i >= 5:
        print(i, "gross")
    elif i <= -5:
        print(i, "klein")
    else:
        print(i)
    i = i - 1
print("-"*50)

# zählt von 0 bis 10 und gibt bei 3,4,5 jeweils den namen als string der zahl aus
i = 0
while i < 11:
    if i == 3:
        print(i, "drei")
    elif i == 4:
        print(i, "vier")
    elif i == 5:
        print(i, "fünf")
    else:
        print(i)
    i = i + 1
print("-"*50)

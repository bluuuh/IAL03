""" Diverse Schleifen
    erstellt von: Mike
    erstellt am : 07.11.22
    geändert am : -

    Das Programm printet Zahlenfolgen die von verschiedenen
    Schleifen generiert werden inklusive extra ausgabe je nach
    Logik der Schleife
    """

# zählt von 100 rückwärts in 10er Schritten und gibt Bingo
# daneben aus wenn die Zahl durch 30 teilbar ist
for i in range(100, 0, -10):
    if i % 30 == 0:
        print(i, "Bingo!")
    else:
        print(i)
print("-"*50)

# zählt von 0 bis 100 und gibt Bingo,Ringo,BingoRingo daneben aus je nachdem
# durch was die Zahl teilbar ist
# Die Datei wird nur zum besseren lesen des Ergebnisses erstellt.
i = 0
BingoRingo = []
while i < 101:
    if i % 5 == 0 and i % 8 == 0:
        BingoRingo.append(str(i)+"Bingo Ringo!")
        print(i, "Bingo Ringo!")
    elif i % 8 == 0:
        BingoRingo.append(str(i)+"Ringo!")
        print(i, "Ringo!")
    elif i % 5 == 0:
        BingoRingo.append(str(i)+"Bingo!")
        print(i, "Bingo!")
    else:
        BingoRingo.append(str(i))
        print(i)
    i = i + 1
with open("Bingo Ringo.txt", "w") as f:
    for items in BingoRingo:
        f.write(items)
        f.write("\n")

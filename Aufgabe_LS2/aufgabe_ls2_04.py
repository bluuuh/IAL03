""" Diverse Listen Operationen
    erstellt von: Mike
    erstellt am : 07.11.22
    geändert am : -

    Es wird eine Liste erstelle und dann verschiedene Listen
    methoden angewand um die Auswirkungen auf die Liste darzustellen
    """

liste = ["Schwalbe", "Kokosnuss", 13, "Spam", 3.14]
liste[2] = 666
print("index", liste)
print("len", len(liste))
liste.append("Ni")
print("append", liste)
liste.extend([4, 5, 3.14])
print("extend", liste)
liste.insert(2, "Taube")
print("insert", liste)
print("count", liste.count(3.14))
print("index", liste.index(3.14))
liste.remove(3.14)
print("remove", liste)
print("pop", liste.pop())
print("pop", liste)
liste.reverse()
print("reverse", liste)

""" Diverse I/O Ausgaben
    erstellt von: Mike
    erstellt am : 07.11.22
    geändert am : -

    Das Programm nimmt eine Zahl vom Anwender und gibt entsprechend
    der Zahl einen Output für den User
    """

# Anwender gibt eine Zahl ein und Ausgabe ist der Name der Zahl
names = ["null", "eins", "zwei", "drei", "vier", "fünf"]
zahl = int(input("Zahl zwischen 0 und 5 eingeben"))
print(zahl, "->", names[zahl])

# Zahl wird vom Anwender eingegeben und es werden diverse
# Eigenschaften der Zahl ausgegeben
zahl = int(input("Ganze Zahl eingeben:"))
vorzeichen = ["-", "+"]
paritaet = ["ungerade", "gerade"]
if zahl >= 0:
    print("Zahl ist positiv")
    positiv = 1
else:
    print("Zahl ist negativ")
    positiv = 0
if zahl % 2 == 0:
    gerade = 1
else:
    gerade = 0
betrag = abs(zahl)
print(f"Deine Zahl ist: {zahl}")
print(f"Deine Zahl ist {paritaet[gerade]}")
print(f"Sie hat das Vorzeichen {vorzeichen[positiv]}")
print(f"Der Betrag ist {betrag}")

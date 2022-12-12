"""
Test ETTZ-22 FS-LF3
Ersteller: Mike Wagner
Datum: 13.12.22022
"""
print("Wagner, Mike (FS-ETTZ-22): LF5 ohne Test ist wie Sylvester ohne Raketen \n\n")

# Eine Liste mit den 4 Datenstrukturen, wird in der Konsole ausgegeben
datenstrukturen = ["List", "Dictionary", "Tuple", "Set"]
print(datenstrukturen, "\n\n")


# schleife die die Zahlen (inklusive) von 31 bis 1 ausgibt, ungerade Zahlen
# printen zusätzlich "bald knallt es"
i = 31
while i >= 1:
    if i % 2 != 0:
        print(f"{i} bald knallt es")
    else:
        print(i)
    i = i - 1
print("\n")


# Feld mit Zahlen die pro Zeile ausgegeben werden
feld = [1, 3, 5, 2, 4]
for zahl in feld:
    print(zahl)
print("\n")


# einfügen der zahl 111 zwischen 1 und 3 in feld
feld.insert(1, 111)


# werte verfünfachen und nach größe sortieren
for index, _wert in enumerate(feld):
    feld[index] = 5 * feld[index]
feld.sort()
for zahl in feld:
    print(zahl)
print("\n")


# Schlüssel Wertepaare einer Sylfesterfeier
sylvesterfeier = {"Rakete": 5, "Sekt": 2,
                  "Wunderkerze": 10, "Büffet": 1, "Böller": 12}
for key in sylvesterfeier:
    print(key, sylvesterfeier[key])
print("\n")


# Gesamtzahl der Elemente der Feier
Summe = 0
for value in sylvesterfeier.values():
    Summe = Summe + value
print(f"Gesamtergebnis: {Summe}")

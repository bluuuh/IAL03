""" Dictionary Einführung
    erstellt von: Mike
    erstellt am : 07.11.22
    geändert am : -

    Einführung in Dictionaries
    """

Adresse = {"Vorname": "Max", "Nachname": "Mustermann", "Strasse": "Musterweg",
           "Hausnummer": 10, "PLZ": 55555, "Ort": "Musterstadt"}
for key, value in Adresse.items():
    print(key, value)
print("--------------------")
for key in Adresse.keys():
    print(key)
print("--------------------")
Adresse["Strasse"] = "Anderestrasse"
Adresse["Hausnummer"] = 11
print("Anzahl der Keys ->", len(Adresse.keys()))
print("--------------------")
Adresse["Land"] = "Deutschland"
print(Adresse)

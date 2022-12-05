""" Listen bearbeiten
    erstellt von: Mike
    erstellt am : 07.11.22
    geändert am : -

    Es wird eine Lise mit einer While Schleife gefühlt und danach
    jedes Element mit einer while Schleife verdoppelt
    """

liste = []
i = 0
j = 0
while i < 11:
    liste.append(i)
    i = i + 1
print(liste)
while j < len(liste):
    liste[j] = 2 * liste[j]
    j = j + 1
print(liste)

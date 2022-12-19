"""Modul für Input/Output mit dem Benutzer
    """


def read_radius():
    """liest Radius ein

    Returns:
        radius: float
    """
    radius = float(input("Radius eingeben(m):"))
    return radius


def output(volumen, oberflaeche):
    """Gibt Volumen & Oberflaeche Aus

    Args:
        volumen (number)
        oberflaeche (number)
    """
    print(f"Volumen: {volumen}m³\nOberfläche: {oberflaeche}m²")

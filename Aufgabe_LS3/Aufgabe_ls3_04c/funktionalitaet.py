from math import pi


def volume(radius):
    """Berechene Kugelvolumen mit dem radius

    Args:
        radius (float): radius der Kugel
    """
    volumen = round((4/3*pi)*radius**3, 2)
    return volumen


def oberflaeche(radius):
    """Berechne Kugeloberfläche mit dem radius

    Args:
        radius (float): radius der Kugel
    """
    oberflaeche = round((4*pi)*radius**2, 2)
    return oberflaeche

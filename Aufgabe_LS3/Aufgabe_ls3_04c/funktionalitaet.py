from math import pi


def calc_volume(radius):
    """Berechene Kugelvolumen mit dem radius

    Args:
        radius (float): radius der Kugel
    """
    volumen = (4/3*pi)*radius**3
    return volumen


def calc_oberflaeche(radius):
    """Berechne Kugeloberfläche mit dem radius

    Args:
        radius (float): radius der Kugel
    """
    oberflaeche = (4*pi)*radius**2
    return oberflaeche

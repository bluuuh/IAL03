

def my_add(a, b):
    """add two numbers

    Args:
        a (float/int)
        b (float/int)

    Returns:
        float/int
    """
    return a + b


def my_sub(a, b):
    """Subtraction

    Args:
        a (float/int)
        b (float/int)

    Returns:
        float/int
    """
    return a - b


def my_div(a, b):
    """division

    Args:
        a (float)
        b (float)

    Returns:
        float
    """
    if b == 0:
        return ZeroDivisionError
    else:
        return a / b


def my_mul(a, b):
    """multiplication

    Args:
        a (float /int)
        b (float /int)

    Returns:
        float /in)
    """
    return a * b

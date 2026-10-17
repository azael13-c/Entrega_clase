
"Calcula una potencia para exponentes enteros no negativos."


def potencia(base: float, exponente: int) -> float:
    if exponente < 0:
        raise ValueError("El exponente debe ser no negativo")
    # Cualquier número elevado a cero vale uno
    if exponente == 0:
        return 1
    # en cada paso reducimos el exponente en uno.
    return base * potencia(base, exponente - 1)


if __name__ == "__main__":
    print(potencia(2, 5))

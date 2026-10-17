"Invierte un texto usando llamadas recursivas"


def invertir(cadena: str) -> str:
    # una cadena vacía ya está invertida
    if cadena == "":
        return ""
    # dejamos el primer carácter para el final y resolvemos el resto.
    return invertir(cadena[1:]) + cadena[0]


if __name__ == "__main__":
    print(invertir("python"))

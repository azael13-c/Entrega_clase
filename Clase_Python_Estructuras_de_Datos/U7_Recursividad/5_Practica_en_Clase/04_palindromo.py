"Comprueba recursivamente si una palabra se lee igual al revés"


def es_palindromo(palabra: str) -> bool:
    # quitamos espacios y no distinguimos entre mayúsculas y minúsculas
    palabra = palabra.lower().replace(" ", "")
    # Con cero o una letra no hay nada que contradiga el palíndromo
    if len(palabra) <= 1:
        return True
    # si los extremos coinciden, revisamos la parte que queda al centro.
    return palabra[0] == palabra[-1] and es_palindromo(palabra[1:-1])


if __name__ == "__main__":
    print(es_palindromo("Anita lava la tina"))

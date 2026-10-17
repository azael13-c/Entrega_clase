"Aplana listas anidadas que contienen enteros"


def flatten(elementos: list) -> list[int]:
    resultado: list[int] = []
    for elemento in elementos:
        if isinstance(elemento, list):
            # la lista interna también puede traer más listas adentro
            resultado.extend(flatten(elemento))
        elif isinstance(elemento, int) and not isinstance(elemento, bool):
            resultado.append(elemento)
        else:
            raise TypeError("Solo se permiten enteros y listas")
    return resultado


if __name__ == "__main__":
    print(flatten([1, [2, [3, 4], 5]]))

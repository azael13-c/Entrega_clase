
"Encuentra el mayor valor de una lista sin usar max()"


def maximo(lista: list[int]) -> int:
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    # en una lista de un elemento, ese ya es el máximo
    if len(lista) == 1:
        return lista[0]
    # El resto de la lista se resuelve con la misma función
    mayor_del_resto = maximo(lista[1:])
    return lista[0] if lista[0] > mayor_del_resto else mayor_del_resto


if __name__ == "__main__":
    print(maximo([4, 9, 1, 12, 3]))

"""Cuenta caminos que solo avanzan abajo o a la derecha"""
from functools import lru_cache


def contar_caminos(filas: int, columnas: int) -> int:
    if filas <= 0 or columnas <= 0:
        raise ValueError("El tablero debe tener dimensiones positivas")

    @lru_cache(maxsize=None)
    def desde(fila: int, columna: int) -> int:
        # la caché evita volver a contar una posición ya visitada
        # Llegar a la esquina final cuenta como un camino
        if fila == filas - 1 and columna == columnas - 1:
            return 1
        if fila >= filas or columna >= columnas:
            return 0
        # sumamos las opciones de bajar y moverse a la derecha.
        return desde(fila + 1, columna) + desde(fila, columna + 1)

    return desde(0, 0)


# con la caché, el tiempo y el espacio son O(filas * columnas)
if __name__ == "__main__":
    print(contar_caminos(3, 4))

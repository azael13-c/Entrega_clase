
"Imprime filas de asteriscos de una hasta n"


def imprimir_patron(n: int) -> None:
    if n < 0:
        raise ValueError("n debe ser cero o positivo")

    def imprimir_fila(fila: int) -> None:
        # cuando la fila supera n, ya imprimimos el patrón completo
        if fila > n:
            return
        # La fila actual tiene tantos asteriscos como indica su número
        print("*" * fila)
        imprimir_fila(fila + 1)

    imprimir_fila(1)


if __name__ == "__main__":
    imprimir_patron(3)

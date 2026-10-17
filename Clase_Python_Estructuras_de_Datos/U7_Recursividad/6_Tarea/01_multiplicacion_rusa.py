
"Multiplica por duplicación y suma, sin usar el operador * "


def multiplicar(a: int, b: int) -> int:
    # separamos el signo para aceptar también números negativos
    signo = -1 if (a < 0) != (b < 0) else 1
    a, b = abs(a), abs(b)

    def acumular(x: int, y: int) -> int:
        # si ya no quedan unidades de y, terminamos
        if y == 0:
            return 0
        # cuando y es impar, x sí forma parte de la suma final.
        if y % 2:
            return x + acumular(x + x, y // 2)
        # en ambos casos duplicamos x y partimos y a la mitad
        return acumular(x + x, y // 2)

    resultado = acumular(a, b)
    return resultado if signo > 0 else -resultado


# cada paso reduce b a la mitad: O(log b) en tiempo y espacio de pila
if __name__ == "__main__":
    print(multiplicar(-7, 6))

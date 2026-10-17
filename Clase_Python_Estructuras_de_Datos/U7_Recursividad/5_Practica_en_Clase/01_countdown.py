"Cuenta hacia atrás y anuncia el despegue"


def countdown(n: int) -> None:
    if n < 0:
        raise ValueError("n debe ser cero o positivo")
    # al llegar a cero ya podemos terminar
    if n == 0:
        print("¡Despegue!")
        return
    print(n)  # mostramos este número antes de bajar al siguiente
    countdown(n - 1)  # cada llamada se acerca al caso base.


if __name__ == "__main__":
    countdown(5)

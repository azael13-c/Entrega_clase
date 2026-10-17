"Cuenta nodos que no tienen hijos"


class Nodo:
    def __init__(self, valor):
        self.valor, self.izquierdo, self.derecho = valor, None, None


def contar_hojas(nodo):
    # None no es una hoja, así que suma cero
    if nodo is None:
        return 0
    if nodo.izquierdo is None and nodo.derecho is None:
        return 1
    return contar_hojas(nodo.izquierdo) + contar_hojas(nodo.derecho)


raiz = Nodo(8)
raiz.izquierdo, raiz.derecho = Nodo(4), Nodo(12)
print(contar_hojas(raiz))

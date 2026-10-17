
"Calcula la altura de un árbol binario"


class Nodo:
    def __init__(self, valor):
        self.valor, self.izquierdo, self.derecho = valor, None, None


def altura(nodo):
    if nodo is None:
        return -1  # contamos la altura en aristas
    # la altura depende de la rama más larga.
    return 1 + max(altura(nodo.izquierdo), altura(nodo.derecho))


raiz = Nodo(10)
raiz.izquierdo, raiz.derecho = Nodo(5), Nodo(15)
print(altura(raiz))

"Muestra la forma de un BST al insertar valores ordenados"


class Nodo:
    def __init__(self, valor):
        self.valor, self.izquierdo, self.derecho = valor, None, None


def insertar(nodo, valor):
    if nodo is None:
        return Nodo(valor)
    # los menores van a la izquierda; los demás se ubican a la derecha
    if valor < nodo.valor:
        nodo.izquierdo = insertar(nodo.izquierdo, valor)
    else:
        nodo.derecho = insertar(nodo.derecho, valor)
    return nodo


def altura(nodo):
    # contamos la altura por aristas, por eso el árbol vacío vale -1
    if nodo is None:
        return -1
    return 1 + max(altura(nodo.izquierdo), altura(nodo.derecho))


raiz = None
for valor in [1, 2, 3, 4, 5]:
    raiz = insertar(raiz, valor)
# al insertar en orden, cada nuevo valor queda más abajo a la derecha
print("Altura:", altura(raiz))  # queda como una cadena hacia la derecha.

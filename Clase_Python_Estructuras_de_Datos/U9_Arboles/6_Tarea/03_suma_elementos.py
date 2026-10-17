"""Suma todos los valores del árbol sin cambiar sus nodos"""


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        def poner(nodo):
            if nodo is None:
                return Nodo(valor)
            if valor < nodo.valor:
                nodo.izquierdo = poner(nodo.izquierdo)
            elif valor > nodo.valor:
                nodo.derecho = poner(nodo.derecho)
            return nodo
        self.raiz = poner(self.raiz)

    def suma(self):
        def sumar(nodo):
            # una rama vacía aporta cero a la suma
            if nodo is None:
                return 0
            # sumamos el nodo actual junto con sus dos subárboles.
            return nodo.valor + sumar(nodo.izquierdo) + sumar(nodo.derecho)
        return sumar(self.raiz)


if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()
    for numero in [8, 3, 10, 1, 6]:
        arbol.insertar(numero)
    print(arbol.suma())

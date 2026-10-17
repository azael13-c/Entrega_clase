"Revisa si cada nodo interno tiene sus dos hijos"


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

    def es_completo(self):
        """En este ejercicio, completo significa que no hay nodos con un hijo."""
        def revisar(nodo):
            if nodo is None:
                return True
            tiene_izquierdo = nodo.izquierdo is not None
            tiene_derecho = nodo.derecho is not None
            # si solo tiene uno de los dos, ya sabemos que no cumple
            if tiene_izquierdo != tiene_derecho:
                return False
            return revisar(nodo.izquierdo) and revisar(nodo.derecho)
        return revisar(self.raiz)


if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()
    for numero in [8, 4, 12, 2, 6, 10, 14]:
        arbol.insertar(numero)
    print(arbol.es_completo())


"Recorre el BST por niveles usando una cola."
from collections import deque


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

    def bfs(self):
        if self.raiz is None:
            return []
        # la cola conserva el orden en que encontramos cada nivel
        resultado, cola = [], deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.valor)
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)
        return resultado


if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()
    for numero in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(numero)
    print(arbol.bfs())

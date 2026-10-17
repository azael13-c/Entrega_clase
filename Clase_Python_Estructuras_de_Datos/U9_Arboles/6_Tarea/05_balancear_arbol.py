
"Reconstruye el BST con una altura mínima para sus valores actuales"


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

    def balancear_arbol(self):
        valores = []
        def guardar(nodo):
            if nodo:
                guardar(nodo.izquierdo)
                valores.append(nodo.valor)
                guardar(nodo.derecho)
        guardar(self.raiz)  # el inorden conserva el orden del BST

        def construir(inicio, fin):
            if inicio >= fin:
                return None
            # el valor central deja cantidades parecidas a ambos lados
            medio = (inicio + fin) // 2
            nodo = Nodo(valores[medio])
            nodo.izquierdo = construir(inicio, medio)
            nodo.derecho = construir(medio + 1, fin)
            return nodo
        self.raiz = construir(0, len(valores))

    def inorden(self):
        resultado = []
        def recorrer(nodo):
            if nodo:
                recorrer(nodo.izquierdo)
                resultado.append(nodo.valor)
                recorrer(nodo.derecho)
        recorrer(self.raiz)
        return resultado


if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()
    for numero in [1, 2, 3, 4, 5, 6, 7]:
        arbol.insertar(numero)
    arbol.balancear_arbol()
    print(arbol.inorden())

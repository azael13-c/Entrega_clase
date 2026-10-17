"BST con eliminación de nodos en sus tres casos"


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
            # Si es igual, lo dejamos como está para no guardar duplicados.
            return nodo
        self.raiz = poner(self.raiz)

    def eliminar(self, valor):
        def quitar(nodo):
            # si llegamos a None, el valor no estaba en el árbol
            if nodo is None:
                return None
            if valor < nodo.valor:
                nodo.izquierdo = quitar(nodo.izquierdo)
            elif valor > nodo.valor:
                nodo.derecho = quitar(nodo.derecho)
            else:
                # si falta un hijo, el otro subárbol ocupa su lugar
                if nodo.izquierdo is None:
                    return nodo.derecho
                if nodo.derecho is None:
                    return nodo.izquierdo
                # con dos hijos usamos el menor valor del lado derecho.
                sucesor = nodo.derecho
                while sucesor.izquierdo:
                    sucesor = sucesor.izquierdo
                nodo.valor = sucesor.valor
                # quitamos la copia del sucesor que acabamos de mover
                nodo.derecho = quitar_sucesor(nodo.derecho, sucesor.valor)
            return nodo

        def quitar_sucesor(nodo, valor_sucesor):
            if valor_sucesor < nodo.valor:
                nodo.izquierdo = quitar_sucesor(nodo.izquierdo, valor_sucesor)
            elif valor_sucesor > nodo.valor:
                nodo.derecho = quitar_sucesor(nodo.derecho, valor_sucesor)
            else:
                return nodo.derecho
            return nodo

        self.raiz = quitar(self.raiz)

    def inorden(self):
        salida = []
        def recorrer(nodo):
            if nodo:
                recorrer(nodo.izquierdo)
                salida.append(nodo.valor)
                recorrer(nodo.derecho)
        recorrer(self.raiz)
        return salida


if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()
    for numero in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(numero)
    arbol.eliminar(50)
    print(arbol.inorden())

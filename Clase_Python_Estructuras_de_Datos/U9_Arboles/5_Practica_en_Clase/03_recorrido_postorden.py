"Recorrido postorden: primero hijos y al final la raíz"


class Nodo:
    def __init__(self, valor):
        self.valor, self.izquierdo, self.derecho = valor, None, None


def postorden(nodo, salida):
    # una rama vacía no agrega nada al recorrido
    if nodo is None:
        return
    postorden(nodo.izquierdo, salida)
    postorden(nodo.derecho, salida)
    salida.append(nodo.valor)


raiz = Nodo(10)
raiz.izquierdo, raiz.derecho = Nodo(5), Nodo(15)
raiz.izquierdo.izquierdo, raiz.izquierdo.derecho = Nodo(2), Nodo(7)
salida = []
postorden(raiz, salida)
print(salida)

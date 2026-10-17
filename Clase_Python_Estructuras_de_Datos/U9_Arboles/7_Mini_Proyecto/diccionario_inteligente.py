
"Diccionario con búsqueda exacta y sugerencias por prefijo en un BST."


class Palabra:
    def __init__(self, texto: str, definicion: str):
        # guardamos en minúscula para que buscar no dependa de cómo escriban la palabra
        self.texto = texto.strip().lower()
        self.definicion = definicion.strip()


class Nodo:
    def __init__(self, palabra: Palabra):
        self.palabra = palabra
        self.izquierdo = None
        self.derecho = None


class Diccionario:
    def __init__(self):
        self.raiz = None

    def agregar(self, palabra: Palabra) -> None:
        def poner(nodo):
            if nodo is None:
                return Nodo(palabra)
            if palabra.texto < nodo.palabra.texto:
                nodo.izquierdo = poner(nodo.izquierdo)
            elif palabra.texto > nodo.palabra.texto:
                nodo.derecho = poner(nodo.derecho)
            else:
                nodo.palabra = palabra  # si ya existe, dejamos la definición nueva
            return nodo
        self.raiz = poner(self.raiz)

    def buscar(self, texto: str) -> Palabra | None:
        texto = texto.strip().lower()
        nodo = self.raiz
        while nodo:
            # como es un BST, cada comparación nos manda a una sola rama
            if texto == nodo.palabra.texto:
                return nodo.palabra
            nodo = nodo.izquierdo if texto < nodo.palabra.texto else nodo.derecho
        return None

    def todas(self) -> list[Palabra]:
        resultado = []
        def recorrer(nodo):
            if nodo:
                # inorden devuelve las palabras en orden alfabético
                recorrer(nodo.izquierdo)
                resultado.append(nodo.palabra)
                recorrer(nodo.derecho)
        recorrer(self.raiz)
        return resultado

    def buscar_por_prefijo(self, prefijo: str) -> list[Palabra]:
        prefijo = prefijo.strip().lower()
        # el recorrido inorden ya entrega las sugerencias en orden alfabético
        return [item for item in self.todas() if item.texto.startswith(prefijo)]


def cargar_diccionario() -> Diccionario:
    entradas = [
        ("árbol", "Estructura jerárquica formada por nodos."),
        ("algoritmo", "Pasos ordenados para resolver un problema."),
        ("arreglo", "Colección de elementos accesibles por posición."),
        ("archivo", "Conjunto de datos guardado con un nombre."),
        ("base", "Parte fundamental de una estructura o sistema."),
        ("búsqueda", "Proceso de localizar un dato."),
        ("byte", "Unidad de información digital de ocho bits."),
        ("cadena", "Secuencia de caracteres."),
        ("ciclo", "Repetición de instrucciones."),
        ("clase", "Molde que define datos y acciones de objetos."),
        ("clave", "Dato usado para identificar o buscar un registro."),
        ("cola", "Estructura que atiende primero al que llegó primero."),
        ("colisión", "Choque entre claves que producen una misma posición."),
        ("compilar", "Traducir código fuente a una forma ejecutable."),
        ("conjunto", "Colección sin elementos repetidos."),
        ("dato", "Representación de un hecho o valor."),
        ("depurar", "Buscar y corregir errores de un programa."),
        ("diccionario", "Colección que relaciona claves con valores."),
        ("dirección", "Ubicación de un dato en memoria."),
        ("duplicado", "Elemento que aparece más de una vez."),
        ("encapsular", "Agrupar datos y operaciones dentro de una unidad."),
        ("estructura", "Forma de organizar datos para trabajar con ellos."),
        ("etiqueta", "Nombre que identifica un elemento."),
        ("flujo", "Orden en que se ejecutan las instrucciones."),
        ("función", "Bloque reutilizable que realiza una tarea."),
        ("grafo", "Conjunto de vértices conectados por aristas."),
        ("hash", "Función que transforma una clave en un valor numérico."),
        ("herencia", "Mecanismo para extender una clase existente."),
        ("índice", "Posición que permite acceder a un elemento."),
        ("instancia", "Objeto creado a partir de una clase."),
        ("iteración", "Repetición de un proceso."),
        ("jerarquía", "Organización por niveles de dependencia."),
        ("lista", "Colección ordenada de elementos."),
        ("memoria", "Espacio donde se guardan datos durante la ejecución."),
        ("método", "Función asociada a una clase u objeto."),
        ("nodo", "Elemento con un valor y enlaces a otros elementos."),
        ("objeto", "Instancia que reúne datos y comportamiento."),
        ("orden", "Disposición de los elementos según un criterio."),
        ("pila", "Estructura que retira primero el último elemento añadido."),
        ("puntero", "Referencia a la ubicación de otro dato."),
        ("raíz", "Nodo inicial de un árbol."),
        ("recorrido", "Visita ordenada de los elementos de una estructura."),
        ("recursividad", "Técnica donde una función se llama a sí misma."),
        ("registro", "Grupo de campos que describen una entidad."),
        ("software", "Conjunto de programas e instrucciones de un sistema."),
        ("secuencia", "Elementos dispuestos en un orden."),
        ("sintaxis", "Reglas para escribir instrucciones válidas."),
        ("tabla", "Estructura que organiza datos en filas o claves."),
        ("tipo", "Categoría que determina valores y operaciones posibles."),
        ("variable", "Nombre asociado a un valor que puede cambiar."),
        ("vértice", "Punto o nodo de un grafo."),
    ]
    diccionario = Diccionario()
    ordenadas = sorted(entradas, key=lambda entrada: entrada[0])

    def insertar_mitad(inicio: int, fin: int) -> None:
        # empezamos por el punto medio para que el árbol no quede como una lista
        if inicio >= fin:
            return
        medio = (inicio + fin) // 2
        texto, definicion = ordenadas[medio]
        diccionario.agregar(Palabra(texto, definicion))
        insertar_mitad(inicio, medio)
        insertar_mitad(medio + 1, fin)

    insertar_mitad(0, len(ordenadas))
    return diccionario


def main() -> None:
    diccionario = cargar_diccionario()
    while True:
        # el menú sigue abierto para poder hacer varias consultas seguidas
        print("\nDiccionario: 1 buscar, 2 prefijo, 3 ver todo, 0 salir")
        opcion = input("Elige: ").strip()
        if opcion == "0":
            break
        if opcion == "1":
            resultado = diccionario.buscar(input("Palabra: "))
            print(resultado.definicion if resultado else "No encontré esa palabra.")
        elif opcion == "2":
            for palabra in diccionario.buscar_por_prefijo(input("Prefijo: ")):
                print(f"{palabra.texto}: {palabra.definicion}")
        elif opcion == "3":
            for palabra in diccionario.todas():
                print(f"{palabra.texto}: {palabra.definicion}")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

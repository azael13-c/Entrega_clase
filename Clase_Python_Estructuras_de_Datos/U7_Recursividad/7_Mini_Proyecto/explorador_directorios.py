"Explora una estructura de carpetas representada con diccionarios"


class ExploradorRecursivo:
    def imprimir_arbol(self, sistema: dict, nivel: int = 0) -> None:
        for nombre, contenido in sistema.items():
            # cada nivel agrega dos espacios para que se note la carpeta madre
            print("  " * nivel + nombre)
            # Los diccionarios representan carpetas; lo demás son archivos
            if isinstance(contenido, dict):
                self.imprimir_arbol(contenido, nivel + 1)

    def buscar_archivo(self, sistema: dict, nombre: str, ruta: str = "") -> str | None:
        for elemento, contenido in sistema.items():
            ruta_actual = f"{ruta}/{elemento}" if ruta else elemento
            if not isinstance(contenido, dict):
                if elemento == nombre:
                    return ruta_actual
            else:
                # probamos dentro de esta carpeta antes de seguir con la siguiente
                encontrado = self.buscar_archivo(contenido, nombre, ruta_actual)
                if encontrado is not None:
                    return encontrado
        # si se acaba este nivel sin hallarlo, no aparece en esta rama
        return None

    def contar_archivos(self, sistema: dict) -> int:
        # cada archivo suma uno; las carpetas solo aportan lo que contienen.
        total = 0
        for contenido in sistema.values():
            if isinstance(contenido, dict):
                total += self.contar_archivos(contenido)
            else:
                total += 1
        return total


if __name__ == "__main__":
    archivos = {
        "Documentos": {
            "apuntes.txt": "10kb",
            "fotos": {"vacaciones.png": "2mb", "perro.jpg": "1mb"},
        },
        "sistema.dll": "500kb",
    }
    explorador = ExploradorRecursivo()
    explorador.imprimir_arbol(archivos)
    print("Ruta:", explorador.buscar_archivo(archivos, "perro.jpg"))
    print("Archivos:", explorador.contar_archivos(archivos))

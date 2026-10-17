"""Cuenta vocales, incluyendo vocales con tilde"""

VOCALES = set("aeiouáéíóúü")


def contar_vocales(texto: str) -> int:
    # el texto vacío marca que ya revisamos todo
    if not texto:
        return 0
    # revisamos una letra y dejamos el resto para la llamada siguiente.
    suma = 1 if texto[0].lower() in VOCALES else 0
    return suma + contar_vocales(texto[1:])


if __name__ == "__main__":
    print(contar_vocales("Estructuras de datos"))

"""

"""


def obtener_detalle(tipo):
    """ """

    diccionario = {"aprobado": "Usted fue aprobado en el curso",
                   "reprobado": "Usted fue reprobado en el curso"}

    for d in diccionario.keys():
        if d == tipo:
            return diccionario[tipo]
    return "tipo equivocado"


if __name__ == "__main__":
    print("Inicio de proceso")
    print(obtener_detalle("reprobado"))


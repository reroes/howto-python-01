"""

"""


def obtener_detalle(tipo):
    """ """

    lista1 = ["aprobado", "reprobado"]
    lista2 = ["Usted fue aprobado en el curso", "Usted fue reprobado en el curso"]

    for d in range(0, len(lista1)):
        if lista1[d] == tipo:
            return lista2[d]
    return "tipo equivocado"


def obtener_detalle_dos(tipo):
    """ """

    lista1 = ["aprobado", "reprobado"]
    lista2 = ["Usted fue aprobado en el curso", "Usted fue reprobado en el curso"]
    lista3 = zip(lista1, lista2)
    for d, e in lista3:
        if d == tipo:
            return e
    return "tipo equivocado"


if __name__ == "__main__":
    print("Inicio de proceso")
    # print(obtener_detalle("aprobado"))
    print(obtener_detalle_dos("aprobado2"))

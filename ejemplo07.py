"""

"""
def obtener_datos():
    """ """
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    edad = input("Ingrese edad: ")
    edad = int(edad)
    cadena = f"Datos Ingresados\n" \
             f"Nombre: {nombre}\n" \
             f"Apellido: {apellido}\n" \
             f"edad: {edad}"
    return cadena


if __name__ == "__main__":
    print("Inicio de proceso")
    mensaje = obtener_datos()
    print(mensaje)

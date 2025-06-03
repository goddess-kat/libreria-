libros = []
prestamos = []
id = []



def crear_libro():
    while True:
        titulo = input("Ingrese Titulo del Libro:\t")
        if titulo == "":
            print("ERROR. Ingrese un nombre del libro")
        else:
            break

    while True:
        autor = input("Autor: ")
        if autor == "":
            print("Ingrese Nombre del Autor:\t")
        else:
            break

    libro = {"titulo": titulo, "autor": autor, "id": len(libros) + 1, "prestado":False}
    return libro


def pre_libro():
    ids = [libro["id"] for libro in libros]
    while True:
        entrada = input("Ingrese id del libro:\t")
        if entrada == "":
            print("ERROR.Ingrese Id del libro")
            continue
        if not entrada.isdigit():
            print("ERROR. Ingrese un número válido")
            continue
        prest = int(entrada)
        if prest <= 0:
            print("ERROR. Ingrese ID válido")
            continue
        if prest not in ids:
            print("ERROR.Ingrese ID existente")
            continue
        for libro in libros:
            if libro["id"] == prest:
                if libro["prestado"]:
                    print("El libro ya está prestado.")
                else:
                    libro["prestado"] = True
                    print("Préstamo Exitoso")
                return
    return prest

def devolver_libro():
    ids = [libro["id"] for libro in libros]
    while True:
        entrada = input("Ingrese id del libro a devolver:\t")
        if entrada == "":
            print("ERROR. Ingrese Id del libro")
            continue
        if not entrada.isdigit():
            print("ERROR. Ingrese un número válido")
            continue
        dev = int(entrada)
        if dev <= 0:
            print("ERROR. Ingrese ID Existente")
            continue
        if dev not in ids:
            print("ERROR. Ingrese ID existente")
            continue
        for libro in libros:
            if libro["id"] == dev:
                if libro["prestado"] == False:
                    print("El libro no está prestado, no puede ser devuelto.")
                else:
                    libro["prestado"] = False
                    print("Gracias por devolver el libro.")
                break
        break
def mostrar_libros():
    if not libros:
        print("No hay libros registrados.")
        return
    print("\n Lista de libros:")
    for libro in libros:
        estado = "Prestado" if libro["prestado"] else "Disponible"
        print("ID:", libro["id"], "| Título:", libro["titulo"], "| Autor:", libro["autor"], "| Estado:", estado)
    print()

def menu():
    while True:
        print("="*10,"Menú","="*10)
        print("1. Ingresar Libro")
        print("2. Prestar Libro")
        print("3. Devolver Libro")
        print("4. Mostrar libros")
        print("5. Salir")
        try:
            op = int(input("Elija una opción:\t"))
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if op == 1:
            libro = crear_libro()
            libros.append(libro)
            print("Se ha agregado:", libro["titulo"])
            print("Del autor:", libro["autor"])
            print("Con la ID:", libro["id"])
        elif op == 2:
            if not libros:
                print("No hay libros registrados.")
            else:
                pre_libro()
        elif op == 3:
            if not libros:
                print("No hay ningún libro registrado.")
            else:
                devolver_libro()
        elif op == 4:
            mostrar_libros()
        elif op == 5:
            print("Gracias,¡Vuelva pronto!...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
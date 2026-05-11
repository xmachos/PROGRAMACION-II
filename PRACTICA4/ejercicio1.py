class Pagina:
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido

    def mostrar_info(self):
        print(f"Página: {self.numero}")
        print(f"Contenido: {self.contenido}")


class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrar_info(self):
        print(f"Autor: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")


class Libro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = []

    def agregar_pagina(self, numero, contenido):
        pagina = Pagina(numero, contenido)
        self.paginas.append(pagina)

    def leer(self):
        print(f"Libro: {self.titulo}")

        for pagina in self.paginas:
            pagina.mostrar_info()
            print("----------------")


class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrar_info(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")


class Horario:
    def __init__(self, dias, apertura, cierre):
        self.dias = dias
        self.apertura = apertura
        self.cierre = cierre

    def mostrar_horario(self):
        print(f"Días: {self.dias}")
        print(f"Apertura: {self.apertura}")
        print(f"Cierre: {self.cierre}")


class Prestamo:
    def __init__(self, fecha_prestamo, fecha_devolucion, estudiante, libro):
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estudiante = estudiante
        self.libro = libro

    def mostrar_info(self):
        print(f"Fecha préstamo: {self.fecha_prestamo}")
        print(f"Fecha devolución: {self.fecha_devolucion}")
        print(f"Estudiante: {self.estudiante.nombre}")
        print(f"Libro: {self.libro.titulo}")


class Biblioteca:
    def __init__(self, nombre, horario):
        self.nombre = nombre
        self.horario = horario
        self.libros = []
        self.autores = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_autor(self, autor):
        self.autores.append(autor)

    def prestar_libro(self, prestamo):
        self.prestamos.append(prestamo)

    def mostrar_estado(self):
        print("===== BIBLIOTECA =====")
        print(f"Nombre: {self.nombre}")

        print("\n--- HORARIO ---")
        self.horario.mostrar_horario()

        print("\n--- LIBROS ---")
        for libro in self.libros:
            print(libro.titulo)

        print("\n--- AUTORES ---")
        for autor in self.autores:
            print(autor.nombre)

        print("\n--- PRÉSTAMOS ---")
        for prestamo in self.prestamos:
            prestamo.mostrar_info()
            print("----------------")

    def cerrar_biblioteca(self):
        self.prestamos.clear()
        print("\nLa biblioteca cerró")
        print("No existen préstamos activos")


horario = Horario(
    "Lunes a Viernes",
    "08:00",
    "20:00"
)

biblioteca = Biblioteca(
    "Biblioteca UMSA",
    horario
)

autor1 = Autor(
    "Gabriel García Márquez",
    "Colombiano"
)

autor2 = Autor(
    "Mario Vargas Llosa",
    "Peruano"
)

biblioteca.agregar_autor(autor1)
biblioteca.agregar_autor(autor2)

libro1 = Libro(
    "Cien años de soledad",
    "12345"
)

libro1.agregar_pagina(
    1,
    "Inicio del libro"
)

libro1.agregar_pagina(
    2,
    "Continuación del libro"
)

libro2 = Libro(
    "La ciudad y los perros",
    "67890"
)

libro2.agregar_pagina(
    1,
    "Capítulo 1"
)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

estudiante1 = Estudiante(
    "2025001",
    "Juan Pérez"
)

prestamo1 = Prestamo(
    "10/05/2026",
    "17/05/2026",
    estudiante1,
    libro1
)

biblioteca.prestar_libro(prestamo1)

biblioteca.mostrar_estado()

print("\n===== LEYENDO LIBRO =====")
libro1.leer()

biblioteca.cerrar_biblioteca()
#lista de productos
global listaProductos
global listaVentas
listaProductos = list()
listaVentas = list()


class Producto:
    codigo = ""
    nombre = ""
    precio = 0
    categoria = ""
    cuantos = ""
    def registrarProducto():
        p = Producto()
        p.codigo = input("Ingrese el código del producto: ")
        p.nombre = input("Ingrese el nombre del producto: ")
        p.precio = input("Ingrese el precio del producto: ")
        p.categoria = input("Ingrese la categoría (abarrote, proteina, lacteo): ")
        p.cuantos = int(input("Ingrese la cantidad: "))
        listaProductos.append(p)
        print("Producto registrado correctamente..!")
        print("")
    def borrarProducto():
        borrado = input("Ingrese el código del producto a borrar: ")
        for p in listaProductos:
            if p.codigo == borrado:
                listaProductos.remove(p)
        print("Producto borrado con éxito..!")
        print("")
    def listarProducto():
        print("Lista de Productos: ")
        for p in listaProductos:
            print (p.codigo, "-", p.nombre, "-", p.precio, "-", p.categoria, "-", p.cuantos)
        print("")


class Venta:
    # numero = 0
    cantidad = 0
    detalle = ""
    total = 0
    medioPago = ""
    def hacerVenta():
        vendido = input("Ingrese el código del producto: ")
        cuanto = int(input("Ingrese cantidad: "))
        tarjeta = input("Ingrese medio de pago (credito ó débito): ")
        for p in listaProductos:
            if p.codigo == vendido:
                v = Venta()
                v.cantidad = cuanto
                v.detalle = p.nombre
                v.total = cuanto * int(p.precio)
                v.medioPago = tarjeta
                listaVentas.append(v)
                p.cuantos = p.cuantos - v.cantidad
        print("Venta exitosa: ")
        print(v.cantidad, "-", v.detalle, "-", v.total, "-", v.medioPago)
        print("")
    def listarVentas():
        print("Lista de Ventas: ")
        for v in listaVentas:
            print (v.cantidad, "-", v.detalle, "-", v.total, "-", v.medioPago)
        print("")
    def salir():
        print("Gracias por usar esta aplicación")
        print("")


class Local:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
    def puntoVenta(self):
        op = 0
        while op != "6":
            print(self.nombre)
            print(self.direccion)
            print("Menú")
            print("1. Registrar Producto")
            print("2. Borrar Producto")
            print("3. Mostrar lista de Productos")
            print("4. Mostrar lista de Ventas")
            print("5. Hacer Venta")
            print("6. Salir")
            op = input("Digite una opción: ")
            if op == "1":
                Producto.registrarProducto()
            elif op == "2":
                Producto.borrarProducto()
            elif op == "3":
                Producto.listarProducto()
            elif op == "4":
                Venta.listarVentas()
            elif op == "5":
                Venta.hacerVenta()
            elif op == "6":
                Venta.salir()
        

nunoa = Local("tia Juanita", "castillo velasco 2385")
nunoa.puntoVenta()



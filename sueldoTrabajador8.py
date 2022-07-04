global listaIsapre
global listaAfp
global listaTrabajadores
listaTrabajadores = list()

listaIsapre = {
    'Consalud': {'descuento':0.13},
    'Banmedica': {'descuento':0.15},
    'Masvida': {'descuento':0.14},
    'Fonasa': {'descuento':0.12},
}

listaAfp = {
    'Cuprum': {'descuento':0.07},
    'Modelo': {'descuento':0.09},
    'Capital': {'descuento':0.12},
    'Provida': {'descuento':0.13},
}


class Trabajador:
    rut = ""
    nombre = ""
    isapre = ""
    afp = ""
    diasTrabajados = 0
    bono = 0
    salario = 0
    bruto = 0
    descuentoIsapreTrabajador = 0
    descuentoAfpTrabajador = 0
    liquido = 0
    def ingresarTrabajador():
        t = Trabajador()
        t.rut = input("Ingrese el rut del trabajador (sin puntos y con guión): ")
        t.nombre = input("Ingrese el nombre del trabajador: ")
        t.isapre = input("Ingrese la isapre del trabajador: ")
        t.afp = input("Ingrese la AFP del trabajador: ")
        t.diasTrabajados = int(input("Ingrese los días trabajados del trabajador: "))
        t.salario = int(input("Ingrese el salario del trabajador: "))
        if t.diasTrabajados >= 20:
            t.bono = 50000
        else:
            t.bono = 0
        listaTrabajadores.append(t)
        print("Trabajador ingresado correctamente..!")
        print("")
    def listarTrabajador():
        print("Lista de trabajadores: ")
        for t in listaTrabajadores:
            print(t.rut, t.nombre, t.isapre, t.afp, t.diasTrabajados, t.salario, t.bono, int(t.bruto), int(t.liquido), sep=" - ", end=".")
        print("")
    def sueldoBruto():
        for t in listaTrabajadores:
            valorDiaTrabajado = t.salario / 20
            t.bruto = (t.diasTrabajados * valorDiaTrabajado) + t.bono
            print(t.rut, "-", t.nombre)
            print("Sueldo Bruto: ", str(int(t.bruto)))
            print("")
    def indemnizacion():
        for t in listaTrabajadores:
            if t.diasTrabajados <= 15:
                indem = t.bruto * 3
                print(t.rut, "-", t.nombre)
                print(t.nombre, "está despedida(o) y su indemnización es: ", str(int(indem)))
                print("")
            else:
                print(t.rut, "-", t.nombre)
                print("No aplica indemnización")
                print("")
    def sueldoLiquido():
        for t in listaTrabajadores:
            t.liquido = t.bruto - (t.descuentoIsapreTrabajador + t.descuentoAfpTrabajador) 
            print(t.rut, "-", t.nombre)
            print("Sueldo Líquido: ", str(int(t.liquido)))
            print("")



class LeyesSociales:
    nombre = ""
    encargado = ""
    def isapre():
        for t in listaTrabajadores:
            if t.isapre == "Consalud":
                t.descuentoIsapreTrabajador = t.bruto * listaIsapre['Consalud']['descuento']
            elif t.isapre == "Banmedica":
                t.descuentoIsapreTrabajador = t.bruto * listaIsapre['Banmedica']['descuento']
            elif t.isapre == "Masvida":
                t.descuentoIsapreTrabajador = t.bruto * listaIsapre['Masvida']['descuento']
            elif t.isapre == "Fonasa":
                t.descuentoIsapreTrabajador = t.bruto * listaIsapre['Fonasa']['descuento']
            print(t.nombre)
            print("El descuento de Isapre es: ", str(int(t.descuentoIsapreTrabajador)))
            print("")
    def afp():
        for t in listaTrabajadores:
            if t.afp == "Cuprum":
                t.descuentoAfpTrabajador = t.bruto * listaAfp['Cuprum']['descuento']
            if t.afp == "Modelo":
                t.descuentoAfpTrabajador = t.bruto * listaAfp['Modelo']['descuento']
            if t.afp == "Capital":
                t.descuentoAfpTrabajador = t.bruto * listaAfp['Capital']['descuento']
            if t.afp == "Provida":
                t.descuentoAfpTrabajador = t.bruto * listaAfp['Provida']['descuento']
            print(t.nombre)
            print("El descuento de AFP es: ", str(int(t.descuentoAfpTrabajador)))
            print("")
    def pagoIsapres():
        pagarIsapres = 0
        for t in listaTrabajadores:
            pagarIsapres += t.descuentoIsapreTrabajador 
        print("El monto a pagar en Isapres es:\n", int(pagarIsapres))
        print("")
    def pagoAfps():
        pagarAfps = 0
        for t in listaTrabajadores:
            pagarAfps += t.descuentoAfpTrabajador 
        print("El monto a pagar en AFPs es:\n", int(pagarAfps))
        print("")
    def pagoPrevired():
        pagarPrevired = 0
        for t in listaTrabajadores:
            pagarPrevired += (t.descuentoIsapreTrabajador + t.descuentoAfpTrabajador)
        print("El monto a pagar en Previred es:\n", int(pagarPrevired))
    def salir():
        print("Gracias por usar estar aplicación..!")
        print("")
        


class RecursosHumanos:
    def __init__(self, empresa, direccion, encargado):
        self.empresa = empresa
        self.direccion = direccion
        self.encargado = encargado
    def main(self):
        op = 0
        while op != "11":
            print(self.empresa)
            print(self.direccion)
            print(self.encargado)
            print("Menú: ")
            print("1. Ingresar trabajador")
            print("2. Mostrar lista de trabajadores")
            print("3. Calcular Sueldo Bruto de los trabajadores")
            print("4. Calcular indemnización de los trabajadores (si aplica)")
            print("5. Calcular descuento de isapre de los trabajadores")
            print("6. Calcular descuento de AFP de los trabajadores")
            print("7. Calcular Sueldo Líquido de los trabajadores")
            print("8. Monto total a pagar en Isapre")
            print("9. Monto total a pagar en AFP")
            print("10. Monto total a pagar en Previred")
            print("11. Salir")
            op = input("Ingrese una opción: ")
            if op == "1":
                Trabajador.ingresarTrabajador()
            elif op == "2":
                Trabajador.listarTrabajador()
            elif op == "3":
                Trabajador.sueldoBruto()
            elif op == "4":
                Trabajador.indemnizacion()
            elif op == "5":
                LeyesSociales.isapre()
            elif op == "6":
                LeyesSociales.afp()
            elif op == "7":
                Trabajador.sueldoLiquido()
            elif op == "8":
                LeyesSociales.pagoIsapres()
            elif op == "9":
                LeyesSociales.pagoAfps()
            elif op == "10":
                LeyesSociales.pagoPrevired()
            elif op == "11":
                LeyesSociales.salir()


brac = RecursosHumanos("Brac", "Alonso de Córdoba 2345", "Felipe Ahumada")
brac.main()






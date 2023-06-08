NumAConvertir = 0
MyLista = []
Numeradores = []
Denominadores = []
Convertido = []

def Suma():
    Iterador = 1
    Res = MyLista[0] + MyLista[1]
    while Iterador + 1 < len(MyLista):
        Iterador += 1
        Res += MyLista[Iterador]
    else:
        print(Res)
        MyLista.clear()
        Menu()

def Resta():
    Iterador = 1
    Res = MyLista[0] - MyLista[1]
    while Iterador + 1 < len(MyLista):
        Iterador += 1
        Res -= MyLista[Iterador]
    else:
        print(Res)
        MyLista.clear()
        Menu()

def Multiplicacion():
    Iterador = 1
    Res = MyLista[0] * MyLista[1]
    while Iterador + 1 < len(MyLista):
        Iterador += 1
        Res *= MyLista[Iterador]
    else:
        print(Res)
        MyLista.clear()
        Menu()

def Division():
    Iterador = 1
    Res = MyLista[0] / MyLista[1]
    while Iterador + 1 < len(MyLista):
        Iterador += 1
        Res /= MyLista[Iterador]
    else:
        print(Res)
        MyLista.clear()
        Menu()

def SumaFracciones():
    Iterador = 1
    Primero = Numeradores[0] * Denominadores[1]
    Segundo = Denominadores[0] * Numeradores[1]
    ResultadoD = Denominadores[0] * Denominadores[1]
    ResultadoN = Primero + Segundo
    while Iterador + 1 < len(Numeradores) and Iterador + 1 < len(Denominadores):
        Iterador += 1
        Primero = ResultadoN * Denominadores[Iterador]
        Segundo = ResultadoD * Numeradores[Iterador]
        ResultadoD *= Denominadores[Iterador]
        ResultadoN = Primero + Segundo
    print(ResultadoN, "/", ResultadoD)

def RestaFracciones():
    Iterador = 1
    Primero = Numeradores[0] * Denominadores[1]
    Segundo = Denominadores[0] * Numeradores[1]
    ResultadoD = Denominadores[0] * Denominadores[1]
    ResultadoN = Primero - Segundo
    while Iterador + 1 < len(Numeradores) and Iterador + 1 < len(Denominadores):
        Iterador += 1
        Primero = ResultadoN * Denominadores[Iterador]
        Segundo = ResultadoD * Numeradores[Iterador]
        ResultadoD *= Denominadores[Iterador]
        ResultadoN = Primero - Segundo
    else:
        print(ResultadoN, "/", ResultadoD)

def MultiplicacionFracciones():
    Iterador = 1
    ResultadoN = Numeradores[0] * Numeradores[1]
    ResultadoD = Denominadores[0] * Denominadores[1]
    while Iterador + 1 < len(Numeradores) and Iterador + 1 < len(Denominadores):
        Iterador += 1
        ResultadoN *= Numeradores[Iterador]
        ResultadoD *= Denominadores[Iterador]
    else:
        print(Numeradores)
        print(Denominadores)
        print(ResultadoN, "/", ResultadoD)

def DivisionFracciones():
    Iterador = 1
    ResultadoN = Numeradores[0] * Denominadores[1]
    ResultadoD = Denominadores[0] * Numeradores[1]
    while Iterador + 1 < len(Numeradores) and Iterador + 1 < len(Denominadores):
        Iterador += 1
        ResultadoN *= Denominadores[Iterador]
        ResultadoD *= Numeradores[Iterador]
    else:
        print(ResultadoN, "/", ResultadoD)

def OperacionesEnteros():
    print("Escriba los numeros de Uno en Uno, cuando haya termina escriba Suma, Resta, Multiplicacion o Division para realizar la operacion indicada")
    OpcionIngresada = input()
    while OpcionIngresada != "Suma" and OpcionIngresada != "Resta" and OpcionIngresada != "Multiplicacion" and OpcionIngresada != "Division":
        if OpcionIngresada.isdigit() == True:
            OpcionInt = int(OpcionIngresada)
            MyLista.append(OpcionInt)
        else:
            OperacionesEnteros()
        OpcionIngresada = input()
    else:
        if OpcionIngresada == "Suma":
            Suma()
        if OpcionIngresada == "Resta":
            Resta()
        if OpcionIngresada == "Multiplicacion":
            Multiplicacion()
        if OpcionIngresada == "Division":
            Division()

def OperacionesFracciones():
    print("Ingrese el Numerador y despues el denominador de la fraccion, repita este proceso hasta que haya ingresado todas las fracciones que desea")
    primero = True
    OpcionFraccion = input()
    while OpcionFraccion != "Suma" and OpcionFraccion != "Resta" and OpcionFraccion != "Multiplicacion" and OpcionFraccion != "Division":
        if OpcionFraccion.isdigit() == True and primero == True:
            IntFraccion = int(OpcionFraccion)
            Numeradores.append(IntFraccion)
            primero = False
        elif OpcionFraccion.isdigit() == True and primero == False:
            IntFraccion = int(OpcionFraccion)
            Denominadores.append(IntFraccion)
            primero = True
        OpcionFraccion = input()
    else:#error actual esta agregando ambos numeros a la misma lista sin importar si primero es true o false FUE CORREGIDO
        if OpcionFraccion == "Suma":
            SumaFracciones()
        if OpcionFraccion == "Resta":
            RestaFracciones()
        if OpcionFraccion == "Multiplicacion":
            MultiplicacionFracciones()
        if OpcionFraccion == "Division":
            DivisionFracciones()
def Conversiones():
    print("")

def Menu():
    print("Escriba 1 para hacer operaciones con enteros, 2 para hacer operaciones con fracciones, 3 para hacer conversion de un numero a otros formatos numericos, 4 para salir del programa")
    NumIngresado = input()
    if NumIngresado == "1":
        OperacionesEnteros()
    if NumIngresado == "2":
        OperacionesFracciones()
    if NumIngresado == "3":
        Conversiones()
    if NumIngresado == "4":
        exit

def Inicio():
    print("Presione On para prender la Calculadora")
    inicio = input()
    if inicio == "On":
        Menu()
    else:
        Inicio()

Inicio()
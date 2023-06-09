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
    print(Res)
    MyLista.clear()
    Menu()

def Resta():
    Iterador = 1
    Res = MyLista[0] - MyLista[1]
    while Iterador + 1 < len(MyLista):
        Iterador += 1
        Res -= MyLista[Iterador]
    print(Res)
    MyLista.clear()
    Menu()

def Multiplicacion():
    Iterador = 1
    Res = MyLista[0] * MyLista[1]
    while Iterador + 1 < len(MyLista):
        Iterador += 1
        Res *= MyLista[Iterador]
    print(Res)
    MyLista.clear()
    Menu()

def Division():
    Iterador = 1
    Res = MyLista[0] / MyLista[1]
    while Iterador + 1 < len(MyLista):
        Iterador += 1
        Res /= MyLista[Iterador]
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
    Numeradores.clear()
    Denominadores.clear()
    Menu()

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
    print(ResultadoN, "/", ResultadoD)
    Numeradores.clear()
    Denominadores.clear()
    Menu()

def MultiplicacionFracciones():
    Iterador = 1
    ResultadoN = Numeradores[0] * Numeradores[1]
    ResultadoD = Denominadores[0] * Denominadores[1]
    while Iterador + 1 < len(Numeradores) and Iterador + 1 < len(Denominadores):
        Iterador += 1
        ResultadoN *= Numeradores[Iterador]
        ResultadoD *= Denominadores[Iterador]
    print(ResultadoN, "/", ResultadoD)
    Numeradores.clear()
    Denominadores.clear()
    Menu()

def DivisionFracciones():
    Iterador = 1
    ResultadoN = Numeradores[0] * Denominadores[1]
    ResultadoD = Denominadores[0] * Numeradores[1]
    while Iterador + 1 < len(Numeradores) and Iterador + 1 < len(Denominadores):
        Iterador += 1
        ResultadoN *= Denominadores[Iterador]
        ResultadoD *= Numeradores[Iterador]
    print(ResultadoN, "/", ResultadoD)
    Numeradores.clear()
    Denominadores.clear()
    Menu()

def ConversionBin(dividendo):
    Cociente, resto = divmod(dividendo, 2)
    Convertido.insert(0, resto)
    while Cociente != 0:
        Cociente, resto = divmod(Cociente, 2)
        Convertido.insert(0, resto)
    print(Convertido)
    Convertido.clear()
    Menu()

def ConversionHex(dividendo):
    Cociente, resto = divmod(dividendo, 16)
    print(resto)
    while Cociente != 0:
        if resto > 9:
            match resto:
                case 10:
                    Convertido.insert(0, "A")
                case 11:
                    Convertido.insert(0, "B")
                case 12:
                    Convertido.insert(0, "C")
                case 13:
                    Convertido.insert(0, "D")
                case 14:
                    Convertido.insert(0, "E")
                case 15:
                    Convertido.insert(0, "F")
        else:
            Convertido.insert(0, resto)
        Cociente, resto = divmod(Cociente, 16)
    Convertido.insert(0, resto)
    print(Convertido)
    Convertido.clear()
    Menu()

def ConversionOct(dividendo):
    Cociente, resto = divmod(dividendo, 8)
    Convertido.insert(0, resto)
    while Cociente != 0:
        Cociente, resto = divmod(Cociente, 8)
        Convertido.insert(0, resto)
    print(Convertido)
    Convertido.clear()
    Menu()

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
    match OpcionIngresada:
        case "Suma":
            Suma()
        case "Resta":
            Resta()
        case "Multiplicacion":
            Multiplicacion()
        case "Division":
            Division()
        case _:
            OperacionesEnteros()

def OperacionesFracciones():
    print("Ingrese el Numerador y despues el denominador de la fraccion, repita este proceso hasta que haya ingresado todas las fracciones que desea. Despues escriba Suma, Resta, Multiplicacion o Divison para realizar la operacion")
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
    match OpcionFraccion:
        case "Suma":
            SumaFracciones
        case "Resta":
            RestaFracciones()
        case "Multiplicacion":
            MultiplicacionFracciones()
        case "Division":
            DivisionFracciones()
        case _:
            OperacionesFracciones()

def Conversiones():
    print("Ingrese un Numero de hasta 4 digitos positivo")
    NumAConvertir = input()
    if NumAConvertir.isdigit() == True and len(NumAConvertir) <= 4:
        NumInt = int(NumAConvertir)
        print("Escriba bin para convertir a binario, hex para convertir a hexadecimal y oct para convertir a octal")
        Ingreso = input()
        match Ingreso:
            case "bin":
                ConversionBin(NumInt)
            case "hex":
                ConversionHex(NumInt)
            case "oct":
                ConversionOct(NumInt)
            case _:
                Conversiones()
    else:
        Conversiones()

def Menu():
    print("Escriba 1 para hacer operaciones con enteros, 2 para hacer operaciones con fracciones, 3 para hacer conversion de un numero a otros formatos numericos, 4 para salir del programa")
    NumIngresado = input()
    match NumIngresado:
        case "1":
            OperacionesEnteros()
        case "2":
            OperacionesFracciones()
        case "3":
            Conversiones()
        case "4":
            exit()
        case _:
            Menu()

def Inicio():
    print("Presione On para prender la Calculadora")
    inicio = input()
    if inicio == "On":
        Menu()
    else:
        Inicio()

Inicio()
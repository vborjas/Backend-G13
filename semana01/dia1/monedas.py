#PROGRAMA PARA CONVERTIR MONEDAS
#VERSION 1.0 - CONVERTIR SOLES A DOLARES
#INPUTS - ENTRADAS
montoOrigen = input("ingrese monto: ")
#PROCESO
opcion = "0"
while(opcion == "0"):
    print("========== Opciones ===========")
    print(" opción 1 - soles a dolares")
    print(" opción 2 - dolares a soles")
    print(" opción 3 - soles a euros")
    print(" opción 4 - euros a soles")
    print(" opcion 5 - Salir")
    print("===============================")
    opcion = input("eliga una opción :")
    if(opcion == "1"):
        montoDolares = float(montoOrigen) / 3.80
        montoDolaresFormato = "$ {:,.2f}".format(montoDolares)
        #OUTPUTS - SALIDAS
        print("El monto en dolares es :" + str(montoDolaresFormato))
    elif(opcion == "2"):
        montoSoles = float(montoOrigen) * 3.80
        montoSolesFormato = "S/. {:,.2f}".format(montoSoles)
        #OUTPUT - SALIDA
        print("El monto en soles es : ",montoSolesFormato)
    elif(opcion == "3"):
        montoSoles = float(montoOrigen) / 4.05
        montoSolesFormato = "€ {:,.2f}".format(montoSoles)
        #OUTPUT - SALIDA
        print("El monto en Euros es:  " , montoSolesFormato)

    elif(opcion == "4"):
        montoEuros = float(montoOrigen) * 4.05
        montoSolesFormato = "S./ {:,.2f}".format(montoEuros)
        #OUTPUT - SALIDA
        print("El monto en Soles es:  " , montoSolesFormato)
    elif(opcion == "5"):
        #OUTPUT - SALIDA
        print("Gracias por usar nuestra Aplicacion") 
    else:
        print("ALERTA !!! debe seleccionar una opción valida")
        opcion = "0"
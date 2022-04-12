#programa para convertir monedas
#VERSION 1.0 CONVERTIR SOLES A DOLARES
#INPUTS - ENTRADAS
from cgi import print_arguments


montoOrigen = input("ingrese el monto en soles:")
#PROCESO
print(" opcion 1 - Soles  a dolares")
print(" opcion 2 - dolares a soles")
print(" opcion 3 - soles a euros")
print(" opcion 4 - euros a soles")
opcion = input("Elija una Opcion :")
if (opcion == 1):
    montoDolares = float(montoOrigen) / 3.80
    montoDolaresFormato = "$ {:,.2f}".format(montoDolares)
    print("El monto en dolares es :" + str(montoDolaresFormato))
elif(opcion == 2):
    montoSoles = float(montoOrigen) * 3.80
    montoSolesFormato = "S/. {:,.2f}".format(montoSoles)
elif(opcion == 3):
    montoEuro = float(montoOrigen) / 4.05
    montoEuroFormato = " {:,.2F}".format()

else:
#OUTPUTS - SALIDAS
    print("El monto en soles es: ", montoSolesFormato)

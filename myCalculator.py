#Calculadora desarrollada por Christian Delgado

activa = True

while activa:

    print("""Bienvenido
    ingrese una de las opciones
    Ingrese '+' para sumar dos numeros
    Ingrese '-' para restar dos numeros
    Ingrese '*' para multiplicar dos numeros
    Ingrese '/' para dividir dos numeros
    Ingrese 'salir' para finalizar""")

    teclado=input(":")

    if teclado=="salir" or teclado=="Salir":
        activa = False
    elif teclado=="+":
        num1=float(input("Ingrese un numero:"))
        num2=float(input("Ingrese otro numero:"))
        result=str(num1+num2)
        print("Respuesta: "+result)
    elif teclado=="-":
        num1=float(input("Ingrese un numero:"))
        num2=float(input("Ingrese otro numero:"))
        result=str(num1-num2)
        print("Respuesta: "+result)
    elif teclado=="*":
        num1=float(input("Ingrese un numero:"))
        num2=float(input("Ingrese otro numero:"))
        result=str(num1*num2)
        print("Respuesta: "+result)
    elif teclado=="/":
        try:
            num1=float(input("Ingrese un numero:"))
            num2=float(input("Ingrese otro numero:"))
            result=str(num1/num2)
            print("Respuesta: "+result)
        except ZeroDivisionError:
            print("Math Error: Division por 0")
    elif teclado=="%":
        try:
            num1=float(input("Ingrese un numero:"))
            num2=float(input("Ingrese otro numero:"))
            result=str(int(num1%num2))
            print("Respuesta: "+result)
        except ZeroDivisionError:
            print("Math Error: Division por 0")
    else:
        print("Opcion inválida")
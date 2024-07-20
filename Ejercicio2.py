def verificar_tributo():
    try:
        edad = int(input("Por favor, ingrese su edad: "))
        ingresos = float(input("Por favor, ingrese sus ingresos mensuales en soles: "))
        
        if edad > 16 and ingresos >= 1000:
            print("Usted tiene que tributar.")
        else:
            print("Usted no tiene que tributar.")
    except ValueError:
        print("Por favor, ingrese valores válidos para la edad y los ingresos.")

verificar_tributo()

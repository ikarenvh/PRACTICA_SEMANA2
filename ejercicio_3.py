#3.- Escribir un programa para una empresa que tiene salas de juegos para
#todas las edades y quiere calcular de forma automática el precio que debe
#cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad
#del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años
#puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de
#18 años, 10€.

#Solución:

edad = int(input("Ingrese su edad: "))

if edad < 4:
    precio = 0
elif edad <=18:
    precio = 5
else:
    precio = 10
    
if precio == 0:
    print("El cliente puede entrar gratis.")    
else:
    print("El precio de la entrada es", precio, "€.")    

    
    


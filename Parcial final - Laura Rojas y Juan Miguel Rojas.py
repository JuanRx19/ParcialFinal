#Procedimiento el cual me permite imprimir el valor final y los productos
def total(id, rol, produc):
    total = 0
    print("La persona cedula " + str(id) + " y rol de " + str(rol) + " compro los siguientes productos: ")
    for elem in produc:
        print("Codigo: " + str(elem))
        print("Nombre: " + str(produc[elem][0]))
        print("Cantidad: " + str(produc[elem][1]) + " unidades\n")
        total += produc[elem][1] * produc[elem][2]
    print("Total a pagar: " + str(total))

#Diccionario creado inicialmente
productosavender = {}
comprar = 1
id = int(input("Por favor digite su cedula: "))
rol = input("Por favor digite su rol (Profesor o Estudiante): ")
#Ciclo el cual me permite repetir la cantidad de veces que un usuario quiera registrar distintos productos
while (comprar != 2):
    producto = int(input("Por favor digite el codigo del producto: "))
    nombre = input("Por favor digite el nombre del producto: ")
    unidades = int(input("Por favor digite la cantidad: "))
    precio = eval(input("Por favor digite el precio del producto: "))
    productosavender[producto] = [nombre, unidades, precio]
    comprar = int(input("¿Desea ingresar otro producto? 1. Si 2. No: "))

#Llamado del procedimiento total, que me permite hacer la impresión
total(id, rol, productosavender)
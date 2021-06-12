#Procedimiento el cual me permite imprimir el valor final y los productos
def total(id, rol, produc):
    totalParcial = 0
    if rol == "Estudiante" or rol == "Profesor":
        print("El " + str(rol) + " con cedula " + str(id) + ", por la compra de los productos: ")
        for elem in produc:
            print("Codigo: " + str(elem))
            print("Nombre: " + str(produc[elem][0]))
            print("Cantidad: " + str(produc[elem][1]) + " unidades")
            print()
            totalParcial += produc[elem][1] * produc[elem][2]
            if rol == "Profesor":
                total = totalParcial - ((totalParcial * 20)/100)
            elif rol == "Estudiante":
                total = (totalParcial * 50)/100
        print("Debe pagar un total de " + str(total))

#Diccionario creado inicialmente
productosavender = {}
comprar = 1
id = int(input("Por favor digite su cedula: "))
p = True
while(p == True):
    try:
        rol = int(input("Por favor digite su rol 1. Profesor o 2. Estudiante: "))
        if(rol == 1):
            rol = "Profesor"
            p = False
        elif(rol == 2):
            rol = "Estudiante"
            p = False
        else:
            print("Por favor digite una opción correcta.")
    except:
        print("Por favor digite una opción correcta.")


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
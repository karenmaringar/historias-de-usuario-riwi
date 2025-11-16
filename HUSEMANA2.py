#primero se debe generar una lista con la palabra inventario 
inventario=[]
#Ahora hacemos una función para no repetir tanto el código
def agregar_el_producto ():
    print ("agregar el producto")

    #se crea variable para pedir el primer dato 
    nombre= input ("ingresar nombre del producto")
    #se crean variables para pedir los otros dos datos precio y cantidad
    while True:

        try:
            precio=float(input("ingresa precio"))
            cantidad=int(input("ingresa cantidad"))
            break 
        except  ValueError:
            print("número incorrecto")

    #se crea diccionario
    producto={"nombre":nombre,
        "precio":precio,
        "cantidad":cantidad}
    
    #se agrega a la lista con append
    inventario.append(producto)
    print ("se agrego exitosamente al inventario")

#se crea otra funcion 
def mostrar_inventario():
    if len(inventario)==0:
        print("el inventario esta vacio")
        return #si el numero de productos es 0 termina la funcion
    
    #se recorre el invenatrio con un bucle for 
    for i in inventario:
        print(f"producto:{i['nombre']}) precio:{i['precio']} cantidad:{i['cantidad']}")


        #se crea otra funcion para las estadisticas
def mostrar_estadisticas():
    if len (inventario) ==0:
        print ("no hay productos para calcular estadisticas")
        return
    
    valor_total=0
    cantidad_total=0

     # Se recorre el inventario
    for i in inventario:
        valor_total += i["precio"] * i["cantidad"]
        cantidad_total += i["cantidad"]

    print(f"Valor total del inventario: {valor_total}")
    print(f"Cantidad total de productos registrados: {cantidad_total}")

#se hace el menu con un bucle while
while True:
    print(" Menu Principal")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadisticas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    # Validación con condicionales y las funciones que hicimos antes
    if opcion == "1":
        agregar_el_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        mostrar_estadisticas()
    elif opcion == "4":
        print("salir")
        break
    else:
        print(" Opción inválida. Intente nuevamente.")


        



    




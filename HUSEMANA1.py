#primero debes crear una variable con un print para el nombre 
nombre=input("ingresa nombre del producto ")

#se debe utilizar un bucle para que vuelva a preguntar si se equivoca 
while True:

    try:
        precio=float(input("ingresa precio ")) #se hace la variable de precio que indique un dato float
        cantidad=int(input("ingresa cantidad "))#variable cantidad indicando un entero
        costo_total=(precio*cantidad) #se multiplica precio por cantidad
        costo_total= print(f"Producto: Lápiz{nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")
        break
    #al final se hace el costo total con todos los datos ingresados
    except ValueError:
        print("ingresa un numero valido")
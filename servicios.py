import csv #Esto se pone hasta arriba para vincular otra libreria.
import json


inventario = []




def cargar_datos():
    """
    Carga los datos almacenados en inventario.json.
    Si el archivo no existe, crea un inventario vacío.
    """
    global inventario
    try:
        with open("inventario.json", "r", encoding="utf-8") as archivo:
            inventario = json.load(archivo)
            print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("No se encontró inventario.json. Se creará cuando guardes datos.")
        inventario = []


def guardar_datos():
    """
    Guarda el inventario completo en un archivo JSON.
    """
    with open("inventario.json", "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4)
    print("Datos guardados correctamente en inventario.json")


def agregar_producto():
    """
    Agrega un producto al inventario solicitando datos al usuario.
    """
    try:
        nombre = input("Ingrese nombre del producto: ").lower()
        precio = float(input("Ingrese precio: "))
        cantidad = int(input("Ingrese cantidad: "))
    except ValueError:
        print("ERROR: Ingrese valores válidos.")
        return

    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print("Producto agregado con éxito.")


def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario.
    """
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\n=== INVENTARIO ===")
    for p in inventario:
        print(f"Nombre: {p['nombre']} - Precio: {p['precio']} - Cantidad: {p['cantidad']}")
    print()


def buscar_producto(nombre):
    """
    Busca un producto por nombre.
    Retorna:
        dict si lo encuentra
        None si no existe
    """
    for p in inventario:
        if p["nombre"] == nombre:
            return p
    return None


def actualizar_producto():
    """
    Actualiza un producto según el nombre.
    """
    nombre = input("Ingrese el nombre del producto a actualizar: ").lower()
    producto = buscar_producto(nombre)

    if not producto:
        print("Producto no encontrado.")
        return

    print("\nProducto encontrado:")
    print(producto)

    print("\n¿Qué desea actualizar?")
    print("1. Nombre")
    print("2. Precio")
    print("3. Cantidad")

    try:
        opcion = int(input("Elija una opción: "))
    except ValueError:
        print("Opción no válida.")
        return

    if opcion == 1:
        producto["nombre"] = input("Nuevo nombre: ").lower()
    elif opcion == 2:
        producto["precio"] = float(input("Nuevo precio: "))
    elif opcion == 3:
        producto["cantidad"] = int(input("Nueva cantidad: "))
    else:
        print("Opción inválida.")
        return

    print("Producto actualizado con éxito.")


def eliminar_producto():
    """
    Elimina un producto del inventario por nombre.
    """
    nombre = input("Nombre del producto a eliminar: ").lower()
    producto = buscar_producto(nombre)

    if not producto:
        print("Producto no encontrado.")
        return

    inventario.remove(producto)
    print("Producto eliminado con éxito.")


def exportar_a_csv():
    """
    Exporta el inventario completo a un archivo CSV.
    """
    if not inventario:
        print("No hay productos para exportar.")
        return

    with open("productos.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "precio", "cantidad"])

        for p in inventario:
            escritor.writerow([p["nombre"], p["precio"], p["cantidad"]])

    print("Datos exportados correctamente a productos.csv")


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.

    Retorna:
        dict con:
            - unidades_totales
            - valor_total
            - producto_mas_caro
            - producto_mayor_stock
    """
    if not inventario:
        print("No hay productos para calcular estadísticas.")
        return None

    subtotal = lambda p: p["precio"] * p["cantidad"]

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }


def mostrar_estadisticas(estadisticas):# Función para mostrar las estadísticas de forma legible
    """
    Muestra las estadísticas del inventario de forma clara.
    """
    print("\n=== ESTADÍSTICAS DEL INVENTARIO ===")
    print(f"Unidades totales: {estadisticas['unidades_totales']}")
    print(f"Valor total: ${estadisticas['valor_total']:.2f}")

    print("\nProducto más caro:")
    print(f"  Nombre: {estadisticas['producto_mas_caro']['nombre']}")
    print(f"  Precio: {estadisticas['producto_mas_caro']['precio']}")

    print("\nProducto con mayor stock:")
    print(f"  Nombre: {estadisticas['producto_mayor_stock']['nombre']}")
    print(f"  Cantidad: {estadisticas['producto_mayor_stock']['cantidad']}")
    print()


#se genera menu para que el usuario pueda ingresar
while True:

    print("\n<==== MENÚ ====>")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Calcular estadísticas")
    print("7. Cargar datos JSON")
    print("8. Guardar datos JSON")
    print("9. Exportar a CSV")
    print("10. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Ingrese un número válido.")
        continue

    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        mostrar_inventario(inventario)
    elif opcion == 3:
        nombre = input("Nombre a buscar: ").lower()
        producto = buscar_producto(nombre)
        print(producto if producto else "Producto no encontrado.")
    elif opcion == 4:
        actualizar_producto()
    elif opcion == 5:
        eliminar_producto()
    elif opcion == 6:
        est = calcular_estadisticas(inventario)
        if est:
            mostrar_estadisticas(est)
    elif opcion == 7:
        cargar_datos()
    elif opcion == 8:
        guardar_datos()
    elif opcion == 9:
        exportar_a_csv()
    elif opcion == 10:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")
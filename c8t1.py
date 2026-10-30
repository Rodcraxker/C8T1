"""
Materia: Sistemas de Control y Programación Avanzada
Tema: Arreglos Unidimensionales y Estructuras (Parte 1)
Descripción: Reto 2 - Sistema básico de gestión de inventario y pedidos 
utilizando arreglos unidimensionales (listas paralelas), funciones y procedimientos.
"""

# Arreglos unidimensionales globales (listas paralelas) para el inventario y pedidos
codigos = []
nombres = []
cantidades = []
precios = []

def mostrar_menu():
    """Procedimiento que despliega el menú principal en consola."""
    print("\n==================================================")
    print("      SISTEMA DE GESTIÓN DE INVENTARIO Y PEDIDOS  ")
    print("==================================================")
    print("1. Registrar nuevo producto o pedido")
    print("2. Mostrar listado actual de inventario")
    print("3. Editar producto o pedido existente")
    print("4. Eliminar producto o pedido del sistema")
    print("5. Salir")
    print("==================================================")

def registrar_producto():
    """Procedimiento para registrar un nuevo elemento en los arreglos unidimensionales."""
    print("\n--- REGISTRAR NUEVO PRODUCTO / PEDIDO ---")
    codigo = input("Ingrese el código único del producto: ").strip()
    
    if codigo in codigos:
        print("¡Error! Ya existe un registro con este código.")
        return
    
    nombre = input("Ingrese el nombre del producto o descripción del pedido: ").strip()
    if not nombre:
        print("¡Error! El nombre no puede estar vacío.")
        return
        
    try:
        cantidad = int(input("Ingrese la cantidad disponible: "))
        precio = float(input("Ingrese el precio unitario ($): "))
    except ValueError:
        print("¡Error! La cantidad y el precio deben ser valores numéricos válidos.")
        return
    
    # Operación de escritura en los arreglos unidimensionales
    codigos.append(codigo)
    nombres.append(nombre)
    cantidades.append(cantidad)
    precios.append(precio)
    print("¡Registro agregado exitosamente al inventario!")

def mostrar_inventario():
    """Procedimiento que recorre e imprime el contenido de los arreglos (Iteración)."""
    print("\n--- LISTADO ACTUAL DE INVENTARIO Y PEDIDOS ---")
    if len(codigos) == 0:
        print("El sistema se encuentra actualmente vacío.")
        return
    
    print(f"{'ÍNDICE':<8} | {'CÓDIGO':<10} | {'DESCRIPCIÓN':<25} | {'CANTIDAD':<10} | {'PRECIO':<10}")
    print("-" * 75)
    
    # Iteración sobre los arreglos unidimensionales usando índices comunes
    for i in range(len(codigos)):
        print(f"{i:<8} | {codigos[i]:<10} | {nombres[i]:<25} | {cantidades[i]:<10} | ${precios[i]:<9.2f}")

def editar_producto():
    """Procedimiento para modificar los datos de un elemento existente en los arreglos."""
    print("\n--- EDITAR PRODUCTO O PEDIDO ---")
    if len(codigos) == 0:
        print("No hay registros disponibles para editar.")
        return
    
    mostrar_inventario()
    try:
        indice = int(input("\nIngrese el índice del elemento que desea editar: "))
        if indice < 0 or indice >= len(codigos):
            print("¡Índice fuera de rango!")
            return
    except ValueError:
        print("¡Por favor ingrese un número entero válido!")
        return
    
    print(f"Editando: {nombres[indice]} (Código actual: {codigos[indice]})")
    
    nuevo_nombre = input(f"Nuevo nombre [{nombres[indice]}]: ").strip()
    if nuevo_nombre:
        nombres[indice] = nuevo_nombre
        
    try:
        nueva_cant_str = input(f"Nueva cantidad [{cantidades[indice]}]: ").strip()
        if nueva_cant_str:
            cantidades[indice] = int(nueva_cant_str)
            
        nuevo_precio_str = input(f"Nuevo precio [{precios[indice]}]: ").strip()
        if nuevo_precio_str:
            precios[indice] = float(nuevo_precio_str)
    except ValueError:
        print("¡Error en los valores numéricos! Los cambios numéricos no se aplicaron.")
        
    print("¡Registro actualizado exitosamente!")

def eliminar_producto():
    """Procedimiento para eliminar elementos de los arreglos unidimensionales por posición."""
    print("\n--- ELIMINAR PRODUCTO O PEDIDO ---")
    if len(codigos) == 0:
        print("No hay registros disponibles para eliminar.")
        return
    
    mostrar_inventario()
    try:
        indice = int(input("\nIngrese el índice del elemento que desea eliminar: "))
        if indice < 0 or indice >= len(codigos):
            print("¡Índice fuera de rango!")
            return
    except ValueError:
        print("¡Por favor ingrese un número entero válido!")
        return
    
    # Eliminación cruzada en todos los arreglos unidimensionales
    c_eliminado = codigos.pop(indice)
    n_eliminado = nombres.pop(indice)
    cantidades.pop(indice)
    precios.pop(indice)
    
    print(f"¡Registro '{n_eliminado}' (Código: {c_eliminado}) eliminado con éxito del sistema!")

def ejecutar_sistema():
    """Función principal que controla el flujo de ejecución mediante un ciclo interactivo."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            mostrar_inventario()
        elif opcion == '3':
            editar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            print("\nSaliendo del sistema de gestión. ¡Hasta luego!")
            break
        else:
            print("¡Opción inválida! Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    ejecutar_sistema()
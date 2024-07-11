from utilidades import *

# Ejecución del programa
productos = []

while True:
    print("\nMenu:")
    print("1) Agregar producto")
    print("2) Calcular la suma de los precios de los productos")
    print("3) Calcular el promedio de los precios de los productos")
    print("4) Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        agregar_producto(productos)
    elif opcion == '2':
        calcular_suma_precios(productos)
    elif opcion == '3':
        calcular_promedio_precios(productos)
    elif opcion == '4':
        guardar_productos_csv(productos)
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")

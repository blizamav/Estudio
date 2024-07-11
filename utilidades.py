import csv
import random

# Definimos una función para agregar un producto
def agregar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    precio = round(random.uniform(10, 100), 2)  # Precio aleatorio entre 10 y 100
    producto = {'nombre': nombre, 'descripcion': descripcion, 'precio': precio}
    productos.append(producto)
    print(f"Producto {nombre} agregado con precio {precio}.")

# Función para calcular la suma de los precios
def calcular_suma_precios(productos):
    suma = sum(producto['precio'] for producto in productos)
    print(f"La suma de los precios de los productos es: {suma}")

# Función para calcular el promedio de los precios
def calcular_promedio_precios(productos):
    if productos:
        promedio = sum(producto['precio'] for producto in productos) / len(productos)
        print(f"El promedio de los precios de los productos es: {promedio}")
    else:
        print("No hay productos para calcular el promedio.")

# Función para guardar los productos en un archivo CSV
def guardar_productos_csv(productos, filename='productos.csv'):
    if productos:
        keys = productos[0].keys()
        with open(filename, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(productos)
        print(f"Productos guardados en el archivo {filename}")
    else:
        print("No hay productos para guardar.")


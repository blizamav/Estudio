import csv
import random
import pandas as pd

# Lista para almacenar los productos
productos = []

# Función para agregar productos a la lista
def agregar_productos(productos):
    while True:
        nombre = input('Ingresa Nombre Producto: ')
        descripcion = input('Ingresa descripcion del producto: ')
        precio = round(random.uniform(10, 100), 2)
        producto = {'nombre': nombre, 'descripcion': descripcion, 'precio': precio}
        productos.append(producto)
        
        continuar = input("¿Quieres agregar otro producto? (si/no): ").strip().lower()
        if continuar != 'si':
            break

    print("Productos agregados:", productos)

# Función para calcular la suma de los precios
def calcular_suma_precios(productos):
    suma = sum(producto['precio'] for producto in productos)
    return suma

# Función para calcular el promedio de los precios usando pandas
def calcular_promedio_precios_pandas(productos):
    df = pd.DataFrame(productos)  # Convertimos la lista de productos en un DataFrame de pandas
    promedio = df['precio'].mean()  # Calculamos el promedio de la columna 'precio'
    return promedio

# Función para guardar los productos en un archivo CSV
def guardar_productos_csv(productos, archivo):
    with open(archivo, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['nombre', 'descripcion', 'precio'])
        writer.writeheader()
        writer.writerows(productos)

# Función para imprimir solo partes específicas de los productos
def imprimir_productos(productos, claves):
    for producto in productos:
        for clave in claves:
            print(f"{clave.capitalize()}: {producto[clave]}")
        print()

# Ejemplo de uso:

# Paso 1: Agregar productos
agregar_productos(productos)

# Paso 2: Calcular la suma de los precios
suma_precios = calcular_suma_precios(productos)
print(f"Suma de precios: {suma_precios}")

# Paso 3: Calcular el promedio de los precios usando pandas
promedio_precios = calcular_promedio_precios_pandas(productos)
print(f"Promedio de precios: {promedio_precios}")

# Paso 4: Guardar los productos en un archivo CSV
guardar_productos_csv(productos, 'productos.csv')

# Paso 5: Imprimir solo los nombres y precios de los productos
imprimir_productos(productos, ['nombre', 'precio'])

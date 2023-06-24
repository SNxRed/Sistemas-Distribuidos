def buscar_datos(nombre):
    with open('name.txt', 'r') as archivo:
        for linea in archivo:
            if nombre in linea:
                inicio_corchetes = linea.index('[')
                fin_corchetes = linea.index(']')
                datos = linea[inicio_corchetes:fin_corchetes+1]
                return datos
    return None

while True:
    nombre_buscado = input("Ingrese el nombre a buscar (o ingrese 0 para salir): ")
    if nombre_buscado == "0":
        break

    datos_encontrados = buscar_datos(nombre_buscado)

    if datos_encontrados:
        print("Datos encontrados:", datos_encontrados)
    else:
        print("No se encontraron datos para el nombre buscado.")

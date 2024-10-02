def validar_opcion (minimo: int, maximo: int):
    opcion = input(f"Seleccione una opción [{minimo} - {maximo}]:")

    if not opcion or not opcion.isdigit() or not (minimo <= int(opcion) <= maximo):
        return validar_opcion(minimo, maximo)
    
    return int(opcion)

if __name__ == '__main__':
    print(validar_opcion(1, 10))
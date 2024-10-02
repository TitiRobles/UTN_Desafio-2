from .auxiliares import obtener_maximo, obtener_minimo, mostrar_heroe
from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes

def filtrar_genero_cantidad(matriz: list[list], genero: str):
    """_summary_ Filtra a los heroes segun el genero que le pasemos

    Args:
        matriz (list[list]): _description_ La matriz con los datos de los heroes
        genero (str): _description_ El genero que necesitemos filtrar
    """
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    for i in range(cantidad_columnas):
        texto = ""
        if matriz[3][i] == genero:
            for s_i in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, s_i, i)}"
            texto = texto[0:-2]
            print(texto)

def filtrar_heroes_poder(matriz: list[list], poder: int):
    """_summary_ Filtra a los heroes por un poder mayor al ingresado

    Args:
        matriz (list[list]): _description_ La matriz con los datos de los heroes
        poder (int): _description_ El poder que necesitemos
    """
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    for i in range(cantidad_columnas):
        texto = ""
        if matriz[4][i] > poder:
            for s_i in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, s_i, i)}"
            texto = texto[0:-2]
            print(texto)

def filtrar_heroes_altura(matriz: list[list], altura: float):
    """_summary_ Filtra a los heroes por una mayor altura a la que ingresemos

    Args:
        matriz (list[list]): _description_ La matriz con los datos de los heroes
        altura (float): _description_ La altura minima que necesitemos
    """
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    for i in range(cantidad_columnas):
        texto = ""
        if matriz[5][i] > altura:
            for s_i in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, s_i, i)}"
            texto = texto[0:-2]
            print(texto)

def filtrar_genero_poder_mas(matriz: list[list], genero: str, poder: int):
    """_summary_ Filtra a los heroes por el genero que ingresemos y por un poder
    mayor al que ingresemos

    Args:
        matriz (list[list]): _description_ La matriz con los datos de los heroes
        genero (str): _description_ El genero que queramos filtrar
        poder (int): _description_ El poder minimo que queramos filtrar
    """
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    for i in range(cantidad_columnas):
        texto = ""
        if matriz[3][i] == genero and matriz[4][i] > poder:
            for s_i in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, s_i, i)}"
            texto = texto[0:-2]
            print(texto)

def filtrar_genero_poder_menos(matriz: list[list], genero: str, poder: int):
    """_summary_ Filtra a los heroes por el genero que ingresemos y por un poder
    menor al que ingresemos

    Args:
        matriz (list[list]): _description_ La matriz con los datos de los heroes
        genero (str): _description_ El genero que queramos filtrar
        poder (int): _description_ El poder maximo que queramos filtrar
    """
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    for i in range(cantidad_columnas):
        texto = ""
        if matriz[3][i] == genero and matriz[4][i] < poder:
            for s_i in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, s_i, i)}"
            texto = texto[0:-2]
            print(texto)

def filtrar_genero_poder_entre(matriz: list[list], genero: str, poder_minimo: int, poder_maximo: int):
    """_summary_ Filtra a los heroes por el genero que ingresemos y por un poder entre
    los dos valores ingresados inclusive

    Args:
        matriz (list[list]): _description_ La matriz con los datos de los heroes
        genero (str): _description_ El genero que queramos filtrar
        poder_minimo (int): _description_ El poder minimo
        poder_maximo (int): _description_ El poder maximo
    """
    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    for i in range(cantidad_columnas):
        texto = ""
        if matriz[3][i] == genero and (poder_minimo<=matriz[4][i]<=poder_maximo):
            for s_i in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, s_i, i)}"
            texto = texto[0:-2]
            print(texto)

def filtrar_poder_minimo(matriz: list[list]):
    """_summary_ Recibe la matriz y la filtra por el poder minimo

    Args:
        matriz (list[list]): La matriz con los datos de los heroes
    """
    poder_minimo = obtener_minimo(matriz_data_heroes, 4)

    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    for i in range(cantidad_columnas):
        texto = ""
        if matriz[4][i] == poder_minimo:
            for s_i in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, s_i, i)}"
            texto = texto[0:-2]
            print(texto)

def filtrar_altura_maxima(matriz: list[list]):
    """_summary_ Recibe la matriz y la filtra por el poder minimo

    Args:
        matriz (list[list]): La matriz con los datos de los heroes
    """
    altura_maxima = obtener_maximo(matriz_data_heroes, 5)

    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)
    for i in range(cantidad_columnas):
        texto = ""
        if matriz[5][i] == altura_maxima:
            for s_i in range(cantidad_filas):
                texto += f"{mostrar_heroe(matriz, s_i, i)}"
            texto = texto[0:-2]
            print(texto)


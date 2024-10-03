from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes
from UTN_Heroes_Dataset.utn_funciones.auxiliares import color_text

def obtener_maximo(matriz: list[list], indice_matriz: int) -> float:
    """_summary_ Recibe una matriz con listas y el parametro del indice de la lista que queremos acceder
    y retorna el numero maximo de esa lista

    Args:
        matriz (list[list]): _description_ La matriz con los datos de los heroes
        indice_matriz (int): _description_ El indice de la lista que queremos acceder

    Returns:
        float: _description_
    """
    numero_maximo = None

    for i in matriz[indice_matriz]:
        if not numero_maximo or numero_maximo < i:
            numero_maximo = i
    
    return float(numero_maximo)

def obtener_minimo(matriz: list[list], indice_matriz: int) -> float:
    """_summary_ Recibe una matriz con listas y el parametro del indice de la lista que queremos acceder
    y retorna el numero minimo de esa lista

    Args:
        matriz (list[list]): _description_ La matriz con los datos de los heroes
        indice_matriz (int): _description_ El indice de la lista que queremos acceder

    Returns:
        float: _description_
    """
    numero_minimo = None

    for i in matriz[indice_matriz]:
        if not numero_minimo or numero_minimo > i:
            numero_minimo = i
    
    return float(numero_minimo)

def mostrar_heroe(matriz, s_i, i) -> str:
    """_summary_ Elabora un texto con los datos de los heroes

    Args:
        matriz (_type_): _description_
        s_i (_type_): _description_
        i (_type_): _description_

    Returns:
        str: _description_
    """
    texto = ""
    texto_original = matriz[s_i][i]

    match texto_original:
                case str():
                    if len(texto_original) >= 20:
                        texto_saneado = texto_original[0:20-1]
                        texto += f"{texto_saneado:{20}} | "
                    else: 
                        texto += f"{texto_original:{20}} | "
                case int():
                    texto += f"{matriz[s_i][i]:03} | "
                case float():
                    texto += f"{matriz[s_i][i]:05.2f} | "
                case _:
                    texto += f"{matriz[s_i][i]} | "
    color_text(texto, "green")
    return texto

def selection_sort_matrices(matriz: list[list], ind_matriz: int, sentido: str) -> list[list]:
    matriz_a_ordenar = matriz.pop(ind_matriz)

    for i in range(len(matriz_a_ordenar)-1):
        i_min = i
        for sub_i in range(i+1, len(matriz_a_ordenar)):
            if (matriz_a_ordenar[sub_i] < matriz_a_ordenar[i_min] and sentido == 'ASC')\
            or (matriz_a_ordenar[sub_i] > matriz_a_ordenar[i_min] and sentido == 'DES'):
                i_min = sub_i

        if i_min != i:
            matriz_a_ordenar[i], matriz_a_ordenar[i_min] = matriz_a_ordenar[i_min], matriz_a_ordenar[i]

            for lista in matriz:
                lista[i], lista[i_min] = lista[i_min], lista[i]

    matriz.insert(ind_matriz, matriz_a_ordenar)

    return matriz
    

# if __name__ e== "__main__":
    # pepe = obtener_minimo(matriz_data_heroes, 5)
    # print(pepe)
    # nombres = ['Remy Le Beau', 'Scott Summers', 'Jean Gray', 'Charles Xavier', 'Sara Howlett']
    # aliases = ['Gambit', 'Cyclops', 'Phoenix', 'Professor X', 'X-23']
    # edades = [32, 29, 30, 54, 16]
    # matriz = [nombres, aliases, edades]

    # prueba = selection_sort_matrices(matriz, 0, 'DES')
    # print(prueba)
from validaciones.validaciones import validar_opcion
from funciones import (mostrar_menu, play_sound, clear_console, filtrar_genero_cantidad, filtrar_heroes_poder,
                    filtrar_heroes_altura, filtrar_genero_poder_mas, filtrar_genero_poder_menos, filtrar_genero_poder_entre, 
                    filtrar_poder_minimo, filtrar_altura_maxima, )

def utn_heroes_app(matriz_data_heroes: list[list]):
    while True:
        mostrar_menu()
        opcion = validar_opcion(1, 13)
        play_sound()

        match opcion:
            case 1:
                filtrar_genero_cantidad(matriz_data_heroes, "Femenino")
                pass
            case 2:
                filtrar_genero_cantidad(matriz_data_heroes,"Masculino")
                pass
            case 3:
                filtrar_heroes_poder(matriz_data_heroes, 75)
                pass
            case 4:
                filtrar_heroes_altura(matriz_data_heroes, 160)
                pass
            case 5:
                filtrar_genero_poder_mas(matriz_data_heroes, "Femenino", 60)
                pass
            case 6:
                filtrar_genero_poder_menos(matriz_data_heroes, "Masculino", 60)
                pass
            case 7:
                filtrar_genero_poder_entre(matriz_data_heroes, "No-Binario", 10, 50)
                pass
            case 8:
                filtrar_poder_minimo(matriz_data_heroes)
                pass
            case 9:
                filtrar_altura_maxima(matriz_data_heroes)
                pass
            case 10:
                pass
            case 11:
                pass
            case 12:
                pass
            case 13:
                break
            case _:
                continue
        clear_console()
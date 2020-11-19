import math

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    #Calcula la distancia euclidiana
    res = math.sqrt( ( pow((x_2 - x_1), 2) ) + ( pow((y_2 - y_1), 2) ) )
	#Devuelve el resultado de la fórmula 
    return res

	#También se le conoce a la fórmula como:
	#distancia entre dos puntos
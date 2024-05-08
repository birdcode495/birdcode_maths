# Practica construcción de función para resolver ecuaciones con estructura aditiva y multiplicativa combinadass


def ecuacion_aditiva(a, b, c, d):

	x = 0
	izq = a + (-a) + c*x
	der = b + (-a) + d*x
	x = der / (c + (-d))

	print("El valor de la incognita es: " ,x)


# Llamada a la función para resolver la ecuación 81 - 3x + 2 - 5x = 91 + 7x + 2 + 2x


ecuacion_aditiva(81+2, 91+2, -3-5, 7+2)
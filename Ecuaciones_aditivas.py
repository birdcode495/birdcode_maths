def ecuacion_aditiva(a, b, c, d):

	x = 0
	izq = a + (-a) + c*x
	der = b + (-a) + d*x
	x = der / (c + (-d))

	print("El valor de la incognita es: " ,x)


ecuacion_aditiva(81+2, 91+2, -3-5, 7+2)
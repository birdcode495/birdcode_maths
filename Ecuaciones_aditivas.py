# Practica construcción de función para resolver ecuaciones con estructura aditiva y multiplicativa combinadass

## Notas:

### En el paso 1 se adiciona el opuesto de a en ambos lados de la ecuación para eliminar terminos sin incognita en el lado izquierdo
### En el paso 2 se adiciona el opuesto de d*x en ambos lados de la ecuación para eliminar terminos con incognita en el lado derecho
### En el tercer paso aplicamos factor común (primer caso de factorización) al lado izquierdo de la ecuación para despejar la incognita
### En el paso 4 expresamos el producto de x (incognita) con los coeficientes conocidos y factorizados como cociente de numeros reales
### En el paso 5 despejamos la incognita en el lado izquierdo de la ecuación


def ecuacion_aditiva(a, b, c, d):

	x = 0
	izq = a + (-a) + c*x   # Paso 1: Desarrollo de código para modelar el lado izquierdo de la ecuación
	der = b + (-a) + d*x   # Paso 1: Desarrollo de código para modelar el lado derechos de la ecuación

	izq = c*x - d*x    # Paso 2
	der = b + (-a) + d*x - d*x   # Paso 2

	izq = x*(c + (-d))   # Paso 3
	der = b + (-a)      # Paso 3

	izq = x*(c + (-d)) / (c + (-d))   # Paso 4
	der = (b + (-a)) / (c + (-d))      # Paso 4

	izq = x                           # Paso 5
	der = (b + (-a)) / (c + (-d))


	x = der   # Paso 6 - final para el despeje de x como incognita a calcular

	print("El valor de la incognita es: " , x)


# Llamada a la función para resolver la ecuación 81 - 3x + 2 - 5x = 91 + 7x + 2 + 2x

ecuacion_aditiva(81+2, 91+2, -3-5, 7+2)
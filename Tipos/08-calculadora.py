n1 = input("Ingresa primer numero ")
n2 = input("Ingresa segundo numero ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multip = n1 * n2
div = n1 / n2

mensaje = f""" 
Para los numeros {n1} y {n2}, 
el resultado la suma es {suma}.
el resultado la resta es {resta}.
el resultado la multipilcación es {multip}.
el resultado la div es {div}.
"""
print(mensaje)
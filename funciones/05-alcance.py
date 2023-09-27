saludo = 25 #La ultilización de variables globales es una mala practica

def saludar():
    global saludo
    saludo = "Hola mundo"
    
    
def saludochanchito():
    saludo = 24
    print(saludo)

resultado1 = saludo + 3
print(resultado1)
saludar()
resultado2 = saludo + 3
print(resultado2) 

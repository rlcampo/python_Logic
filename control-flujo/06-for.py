buscar  = 10
arr = [1, 1, 1, 4, 6]
for numero in arr:
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else:
    print("No encontré el numero buscado :(")    
    
for char in "Ultimate python":
    print(char)
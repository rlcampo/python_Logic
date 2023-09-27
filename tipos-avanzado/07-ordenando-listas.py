numeros = [2, 4, 6, 1, 7, 9 , 10, 72]

#numeros.sort(reverse = True)
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [["Chanchito", 4],
            ["Felipe", 1],
            ["Pulga", 5]]


    
usuarios.sort(key=lambda el:el[1])
print(usuarios)
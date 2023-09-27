print("Bienvenido a la calculadora")
print("Para salir dijite salir")
print("Las operaciones son suma, multi, div y resta")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa operación: ")
    if op.lower() == "salir":
        break  
    n2 = input("Ingresa siguiente número: ")
    if n2.lower() == "salir":
        break  
    n2 = int(n2)
    
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no valida")
        break
    
    print(f"El resultado es {resultado}")
    
    
    

# n = input("Digite un número: ")
# oper = " "

# for n in int:
#     if n == int:
#         oper = input("ingrese una operación: {suma}, {resta}, {multi}, {div}")
#         m = input("Ingrese otro número: ")
#         if n.lower() == "salir":
#                 break
#     else:
#         n = input("Por favor digite un número: ")
#         if n.lower() == "salir":
#                 break

# # n = int(n)
# m = int(m)
# suma= n + m
# resta = n - m
# multi = n * m
# div = n / m

# for m in int:
#     if oper == {suma}:
#         mensaje = f""" El resultado de la operación es {suma}"""
#         n = suma
#         oper = input("ingrese una operación: {suma}, {resta}, {multiplicación}, {division}")
#         m = input("Ingrese otro número: ")
#         if m.lower == "salir":
#             break   
#     elif oper == {resta}:
#         mensaje = f""" El resultado de la operación es {resta}"""
#         n = resta
#         oper = input("ingrese una operación: {suma}, {resta}, {multiplicación}, {division}")
#         m = input("Ingrese otro número: ")
#         if m.lower == "salir":
#             break   
#     elif oper == {multi}:
#         mensaje = f""" El resultado de la operación es {multi}"""
#         n = multi
#         oper = input("ingrese una operación: {suma}, {resta}, {multiplicación}, {division}")
#         m = input("Ingrese otro número: ")
#         if m.lower == "salir":
#             break   
#     elif oper == {div}:
#         mensaje = f""" El resultado de la operación es {div}"""
#         n = div
#         oper = input("ingrese una operación: {suma}, {resta}, {multiplicación}, {division}")
#         m = input("Ingrese otro número: ")
#         if m.lower == "salir":
#             break   

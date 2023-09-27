def no_space(texto):
    nuevo_texto = ""
    for char in texto: #Este for lo que hace es que elimina los espacios de una oración si es que existen.
        if char != " ": #Esto lo hace mediante la comparación de si existe un espacio en alguna de las partes
            nuevo_texto += char  #Del texto y si las hay mediante todo el recorrido del vector este eliminará el espacio.
    return nuevo_texto

def reverse(texto):
    texto_al_reves = ""
    for char in texto: #Esta función le da vuelta a un vector formado por texto (Char). 
        texto_al_reves = char + texto_al_reves #Esto lo hace mediante la concatenación del char sumado con la
    return texto_al_reves #variable "texto_al_reves" la cual está vacia al inicio pero luego al ser sumada
                        # simplemente concatena al lado izquierdo en vez del derecho para así invertir el vector.

def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()
    
    print(texto_al_reves)
    
    
print(es_palindromo("Amo la paloma"))
print(es_palindromo("Hola mundo"))
print(es_palindromo("ReConocer"))
print(es_palindromo("Somos o no Somos"))
        
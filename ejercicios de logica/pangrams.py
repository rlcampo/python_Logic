# abc = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "ñ", "l", "k", "j", "h", "g", "f", "d", "s", "a", "z", "x", "c", "v", "b", "n", "m"]
# # #abc = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "ñ", "l", "k",
# #        "j", "h", "g", "f", "d", "s", "a", "z", "x", "c", "v", "b", "n", "m"}
# freq = [0]*len(abc)

# s = "We promptly judged antique ivory buckles for the next prize"
# # print(len(s))

# for letra in abc:
#     if letra not in s:
#         print("Not pangram")
#     else:
#         print("Pangram")


# def es_pangram(s):
#     abc = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "ñ", "l", "k", "j", "h", "g", "f", "d", "s", "a", "z", "x", "c", "v", "b", "n", "m"]

#     for letra in abc:
#         if letra not in s:
#             return "Not pangram"
#     return "Pangram"

# def es_pangrama(cadena):
#     import string
#     cadena = cadena.lower()  # Convertir a minúscula
#     alfabeto = string.ascii_lowercase + "ñ"  # Hablamos español, si no, quítale la ñ
#     for letra in alfabeto:  #Recorrer el alfabeto
#         if letra not in cadena:  # Si una letra del alfabeto no está, sabemos que no es pangrama
#             return False
#     # Si recorrimos todas las letras, terminamos el ciclo
#     # y por lo tanto todas estuvieron, así que:
#     return True


# abecedario="abcdefghijklmnñopqrstuvwxyz"
 
# cadena="el pato volo por la mañana"
 
# faltan=False
# for i in abecedario:
#     if not i in cadena:
#         faltan=True
#         break
 
# if faltan==False:
#     print("Estan todas las letras")
# else:
#     print("no estan todas las letras")
    
# def es_pangram(s):
#     abecedario="abcdefghijklmnñopqrstuvwxyz"
#     faltan = False
#     for i in abecedario:
#         if not i in s:
#             faltan = True
#             break
#     if faltan == False:
#         return "Pangram"
#     else:
#         return "Not pangram"

def pangrams(s):
    # Write your code here
    res = re.sub("[^0-9a-zA-Z]+",'',s.lower())
    is_pan = len(set(res)) == 26
    return 'pangram' if is_pan else 'not pangram'
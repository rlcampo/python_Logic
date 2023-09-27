# decimal = 28
# binario = ""
def decimal_a_binario(decimal):
    if decimal <= 0: 
        return "0" * 32
    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
        vbits = "0" * (int(32) - len(binario))
    binario = vbits + binario
    return binario

decimal = int(input("Ingresa un número decimal: "))
binario = decimal_a_binario(decimal)
print(f"El numero {decimal} es {binario} en binario de 32 bits")


def inv_binario(binario):
    binario = decimal_a_binario(decimal)
    binarioinv = ""
    for n in binario:
        if n == "1":
            binarioinv = "0" + binarioinv
        else:
            binarioinv = "1" + binarioinv
    binarioinv1 = ""
    for n in binarioinv:
        binarioinv1 = n + binarioinv1
        binarioinv = binarioinv1
    return binarioinv
    

binarioinv = inv_binario(binario)
print(f"El numero {binarioinv} es el binario flipeado")

def binario_a_decimal(binarioinv):
    n_decimal = 0
    for posicion, d_string in enumerate(binarioinv[::-1]):
        n_decimal += int(d_string)* 2 ** posicion
    return n_decimal

decimaln = binario_a_decimal(binarioinv)
print(f"El numero {decimaln} es el decimal del binario flipeado")
# while decimal >= 0:
#     residuo = int(decimal % 2)
#     decimal = int(decimal / 2)
#     binario = str(residuo) + binario
# print(binario)
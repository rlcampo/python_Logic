s = "12:45:22PM"
militarhA = ""
militarhM = ""
fh = ""
militarhP = ""
militarhP1 = ""
    
for char in s:
    #print(char)
    if char != "A":
        militarhA += char       
    
for char in militarhA:
    if char != "M":
        militarhM += char        

for char in militarhM:
    if char != "P":
        militarhP += char
        fh = (int(militarhP[:2]) + 12)
        fh = str(fh) + str(militarhP[2:])

for n in s:
     if n == "P" and s[:2] == "12":
         print(militarhP)
     elif n == "P":
        print(fh)
     elif n == "A" and s[:2] == "12":
        print("00" + militarhM[2:])
     elif n == "A":
         print(militarhM)
   
#print(militarhM)  
# #print(militarhM)
# print(militarhP[:2])
# print(fh)
#print(militarhP1)
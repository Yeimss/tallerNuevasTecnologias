cantidad=int(input("ingrese la cantidad de números que desea ingresar: "))
multiplos2=0
multiplos3=0
for i in range(cantidad):
    numero=int(input("Ingrese un numero: "))
    if numero%2==0:
        multiplos2+=1
    if numero%3==0:
        multiplos3+=1

print(f"Multiplos de 2: {multiplos2}")
print(f"Multiplos de 3: {multiplos3}")
